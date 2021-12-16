from model import unloadedCheescakeItem


class ProductsComposer:
    def __init__(self, products_dict):
        self.products_dict = products_dict
        # отчет cheescake
        self.uchList = self.products_dict.pop("Отчет чизкейк")
        self.comparisionList = self.products_dict.pop("Таблица соответствий")

    def create_result(self):
        result_list = []
        for comparision_item in self.comparisionList:

            uch_item = self.get_uchItem(comparision_item.holding_article)

            price_with_expenses = self.get_price_expenses(uch_item.purchase_price,
                                                          uch_item.supplier)

            result_item = {"Холдинг, артикул": comparision_item.holding_article,
                           "Холдинг, наименование": comparision_item.holding_name,
                           "Холдинг, группа": comparision_item.holding_group,
                           "Холдинг, цена закупки с учетом прочих расходов": price_with_expenses,
                           "Холдинг, цена продажи": uch_item.selling_price,
                           "Холдинг, остатки": uch_item.stock,
                           "Холдинг, поставщик": uch_item.supplier,
                           "Холдинг, дата размещения": uch_item.orderDate}

            for supplier_name in self.products_dict:
                my_dict = self.get_supplier_params(supplier_name,
                                                   self.products_dict.get(supplier_name),
                                                   comparision_item.get_values(supplier_name),
                                                   uch_item.selling_price)
                result_item.update(my_dict)

            result_list.append(result_item)
        return result_list



    def get_supplier_params(self, supplier_name, products_list, supplier_articles_brands_dict, holding_price):
        my_dict = {}
        # индекс = количеству столбцов с поставщиком в итоговом файле пример: Дарси 1, артикул  Дарси 2, артиклу
        index = 0
        # итерация по словарю {артикул_поставщика: бренд}
        for supplier_article in supplier_articles_brands_dict:
            if str(supplier_article) == "nan" or supplier_article == 0 or str(supplier_article) == "0.0" or str(supplier_article) == "0":
                pass
            else:
                index += 1
                # итерация по листу с продуктами
                for product in products_list:
                    # если артикул_продукта == артикулу_поставщика
                    # if supplier_article == product.article for product in products_list
                    #print(f'product.article:{product.article} supplier_article:{supplier_article}')
                    if product.article == supplier_article:
                        # добавляем словарь с данными по поставщику: артикул, цену, разницу в цене в %, бренд
                        my_dict.update(self.create_supplier_item_data(supplier_article,
                                                                      product.price,
                                                                      holding_price,
                                                                      supplier_articles_brands_dict.get(supplier_article),
                                                                      supplier_name,
                                                                      index))
        return my_dict


    # создает словрь с данными поставщика артикул, цена, разницу в цене в %, бренд
    def create_supplier_item_data(self, supplier_article, supplier_price,holding_price , brand, supplier_name, index):
        my_dict = {f'{supplier_name} {index}, артикул': supplier_article,
                   f'{supplier_name} {index}, цена': self.get_price_without_nds(supplier_price),
                   f'{supplier_name} {index}, разница цен в %': self.get_procent_difference(supplier_price, holding_price),
                   f'{supplier_name} {index}, бренд': brand}
        return my_dict


    def get_price_without_nds(self, price):
        return f'{self.get_float_from_price(price) / 1.2:.2f}'

    def get_uchItem(self, article):
        for uch_item in self.uchList:
            if article == uch_item.article:
                return uch_item
        return unloadedCheescakeItem.UnloadedCheescakeItem()

    #arr1 = [[123, 234, 456], [923, 934, 956]]
    #find = 923
    #a = [item1 for item in arr1 for item1 in item if item1 == find]



    def get_procent_difference(self, supplier_price, holding_price):
        if holding_price == 0 or holding_price == "0" or supplier_price == 0.00 or supplier_price == "0.00" or supplier_price == "":
            return ""
        # price_holding = float(price_holding)
        p_hold = self.get_float_from_price(self.get_price_without_nds(holding_price))
        p_sup = self.get_float_from_price(supplier_price)
        one_procent = p_hold / 100
        procent = (p_sup / one_procent) - 100
        return f'{procent:.2f}%'


    def get_price_expenses(self, holding_purchase_price, holding_supplier_brand):
        if holding_supplier_brand == "SHAN DONG DONGPING JIUXIN HARDWARE TOOLS CO.,LTD" or \
                holding_supplier_brand == "QINGDAO LEAD WORLD IMP&EXP CO., LTD":
            return self.get_float_from_price(holding_purchase_price) * 1.2
        elif holding_supplier_brand == "SHANGHAI UNI-STAR INDUSTRIAL & TRADING CO., LTD":
            return self.get_float_from_price(holding_purchase_price) * 1.1
        else:
            return self.get_float_from_price(holding_purchase_price)


    def get_float_from_price(self, price):
        try:
            return float(price)
        except:
            #print(price)
            return 0
