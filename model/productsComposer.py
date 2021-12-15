from model import unloadedCheescakeItem


class ProductsComposer:
    def __init__(self, products_dict):
        self.products_dict = products_dict
        self.uchList = self.products_dict.pop("Отчет чизкейк")
        self.comparisionList = self.products_dict.pop("Таблица соответствий")

    def create_result(self):
        result_list = []
        for comparision_item in self.comparisionList:
            uch_item = self.get_uchItem(comparision_item.holding_article, self.uchList)
            purchase_price_with_other_expenses = self.get_price_with_other_expenses(
                self.get_float_from_price(uch_item.purchase_price),
                uch_item.supplier)
            result_item = {"Холдинг, артикул": comparision_item.holding_article,
                           "Холдинг, наименование": comparision_item.holding_name,
                           "Холдинг, группа": comparision_item.holding_group,
                           "Холдинг, цена закупки с учетом прочих расходов": purchase_price_with_other_expenses,
                           "Холдинг, цена продажи": uch_item.selling_price,
                           "Холдинг, остатки": uch_item.stock,
                           "Холдинг, поставщик": uch_item.supplier,
                           "Холдинг, дата размещения": uch_item.orderDate}

            for supplier_name in self.products_dict:
                supplier_articles_brands_list = self.get_supplier_article_brand_list(supplier_name, comparision_item)
                my_dict = self.get_supplier_params(supplier_name, self.products_dict.get(supplier_name),
                                                   supplier_articles_brands_list)
                result_item.update(my_dict)

            result_list.append(result_item)
        return result_list



    def get_supplier_params(self, supplier_name, products_list, supplier_articles_brands_list):
        my_dict = {}
        for article_brand_dict in supplier_articles_brands_list:
            for supplier_article in article_brand_dict:
                for product in products_list:
                    if product.article == supplier_article:
                        my_dict.update(self.create_supplier_item_data(supplier_article, product.price, article_brand_dict.get(supplier_article), supplier_name))
        return my_dict

    def create_supplier_item_data(self, article, price, brand, supplier_name):
        my_dict = {f'{supplier_name}, артикул': article,
                   f'{supplier_name}, цена': price,
                   f'{supplier_name}, разница цены в %': price,
                   f'{supplier_name}, бренд': brand}
        return my_dict



    def get_supplier_article_brand_list(self, supplier_name, comparision_item):
        if supplier_name == "Автоключ":
            return [{comparision_item.avtokluch_article: comparision_item.avtokluch_brand}]
        elif supplier_name == "Дарси":
            return [{comparision_item.darsi1_article: comparision_item.darsi1_brand},
                    {comparision_item.darsi2_article: comparision_item.darsi2_brand}]
        elif supplier_name == "Ипц":
            return [{comparision_item.inpo_article: comparision_item.inpo_brand}]
        elif supplier_name == "Белый медведь":
            return [{comparision_item.whiteBear_article: comparision_item.whiteBear_brand}]
        elif supplier_name == "Мир инструментов":
            return [{comparision_item.mirInstrumentov1_article: comparision_item.mirInstrumentov1_brand},
                    {comparision_item.mirInstrumentov2_article: comparision_item.mirInstrumentov2_brand}]
        return []

    def get_uchItem(self, article, uchList: list):
        for item in uchList:
            if article == item.article:
                return item
        ui = unloadedCheescakeItem.UnloadedCheescakeItem()
        return ui

    def get_float_from_price(self, price):
        if type(price) == int or type(price) == float:
            return price
        else:
            try:
                return float(price)
            except:
                print(price)
                return 0

    def get_price_with_other_expenses(self, price, brand):
        if brand == "SHAN DONG DONGPING JIUXIN HARDWARE TOOLS CO.,LTD" or \
                brand == "QINGDAO LEAD WORLD IMP&EXP CO., LTD":
            return price * 1.2
        elif brand == "SHANGHAI UNI-STAR INDUSTRIAL & TRADING CO., LTD":
            return price * 1.1
        else:
            return price
