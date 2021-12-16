from model import unloadedCheescakeItem


class ResultCreater:
    def __init__(self, products_dict):
        self.products_dict = products_dict
        self.uchList = self.products_dict.get("Отчет чизкейк")
        self.comparisionList = self.products_dict.get("Таблица соответствий")

    def createResultList(self):
        resultList = []
        for comparisionItem in self.comparisionList:
            uchItem = self.get_uchItem(comparisionItem.holding_article, self.uchList)
            price_darsi_1 = self.getSupplierParam(self.products_dict, "Дарси",
                                                  comparisionItem.darsi1_article)
            price_darsi_2 = self.getSupplierParam(self.products_dict, "Дарси",
                                                  comparisionItem.darsi2_article)
            price_avtokluch = self.getSupplierParam(self.products_dict, "Автоключ",
                                                    comparisionItem.avtokluch_article)
            price_inpo = self.getSupplierParam(self.products_dict, "Ипц",
                                               comparisionItem.inpo_article)
            price_white_bear = self.getSupplierParam(self.products_dict, "Белый медведь",
                                                     comparisionItem.whiteBear_article)
            price_mir_instrumetnov_1 = self.getSupplierParam(self.products_dict, "Мир инструментов",
                                                             comparisionItem.mirInstrumentov1_article)
            price_mir_instrumetnov_2 = self.getSupplierParam(self.products_dict, "Мир инструментов",
                                                             comparisionItem.mirInstrumentov2_article)
            purchase_price = self.get_float_from_price(uchItem.purchase_price)
            purchase_price_with_other_expenses = self.get_price_with_other_expenses(purchase_price, uchItem.supplier)
            resultList.append({"Холдинг, артикул": comparisionItem.holding_article,
                               "Холдинг, наименование": comparisionItem.holding_name,
                               "Холдинг, группа": comparisionItem.holding_group,
                               "Холдинг, цена закупки с учетом прочих расходов": purchase_price_with_other_expenses,
                               "Холдинг, цена продажи": uchItem.selling_price,
                               "Холдинг, остатки": uchItem.stock,
                               "Холдинг, поставщик": uchItem.supplier,
                               "Холдинг, дата размещения": uchItem.orderDate,

                               "Автоключ, артикул": comparisionItem.avtokluch_article,
                               "Автоключ, цена": price_avtokluch,
                               "Автоключ, разница в цене": self.get_procent_difference(price_avtokluch,
                                                                                       uchItem.selling_price),
                               "Автоключ, бренд": comparisionItem.avtokluch_brand,

                               "Дарси 1, артикул": comparisionItem.darsi1_article,
                               "Дарси 1, цена": price_darsi_1,
                               "Дарси 1, разница в цене": self.get_procent_difference(price_darsi_1,
                                                                                      uchItem.selling_price),
                               "Дарси 1, бренд": comparisionItem.darsi1_brand,

                               "Дарси 2, артикул": comparisionItem.darsi2_article,
                               "Дарси 2, цена": price_darsi_2,
                               "Дарси 2, разница в цене": self.get_procent_difference(price_darsi_2,
                                                                                      uchItem.selling_price),
                               "Дарси 2, бренд": comparisionItem.darsi2_brand,

                               "Ипц, артикул": comparisionItem.inpo_article,
                               "Ипц, цена": price_inpo,
                               "Ипц, разница в цене": self.get_procent_difference(price_inpo, uchItem.selling_price),
                               "Ипц, бренд": comparisionItem.inpo_brand,

                               "Белый медведь, артикул": comparisionItem.whiteBear_article,
                               "Белый медведь, цена": price_white_bear,
                               "Белый медведь, разница в цене": self.get_procent_difference(price_white_bear,
                                                                                            uchItem.selling_price),
                               "Белый медведь, бренд": comparisionItem.whiteBear_brand,

                               "Мир инструментов 1, артикул": comparisionItem.mirInstrumentov1_article,
                               "Мир инструментов 1, цена": price_mir_instrumetnov_1,
                               "Мир инструментов 1, разница в цене": self.get_procent_difference(
                                   price_mir_instrumetnov_1, uchItem.selling_price),
                               "Мир инструментов 1, бренд": comparisionItem.mirInstrumentov1_brand,

                               "Мир инструментов 2, артикул": comparisionItem.mirInstrumentov2_article,
                               "Мир инструментов 2, цена": price_mir_instrumetnov_2,
                               "Мир инструментов 2, разница в цене": self.get_procent_difference(
                                   price_mir_instrumetnov_2, uchItem.selling_price),
                               "Мир инструментов 2, бренд": comparisionItem.mirInstrumentov2_brand,
                               })
        return resultList

    def getSupplierParam(self, products_dict, file_tag, article):
        if file_tag in products_dict:
            for supplierProduct in products_dict.get(file_tag):
                if str(supplierProduct.article) == article:
                    return f'{self.get_float_from_price(supplierProduct.price) / 1.2:.2f}'
        return ""


    def get_procent_difference(self, price_supplier, price_holding):
        if price_holding == 0 or price_holding == "0" or price_supplier == 0.00 or price_supplier == "0.00" or price_supplier == "":
            return ""
        p_hold = self.get_float_from_price(price_holding)
        p_sup = self.get_float_from_price(price_supplier)
        one_procent = p_hold / 100
        procent = (p_sup / one_procent) - 100
        return f'{procent:.2f}%'

    @staticmethod
    def get_price_with_other_expenses(price, brand):
        if brand == "SHAN DONG DONGPING JIUXIN HARDWARE TOOLS CO.,LTD" or \
                brand == "QINGDAO LEAD WORLD IMP&EXP CO., LTD":
            return price * 1.2
        elif brand == "SHANGHAI UNI-STAR INDUSTRIAL & TRADING CO., LTD":
            return price * 1.1
        else:
            return price

    @staticmethod
    def get_float_from_price(price):
        if type(price) == int or type(price) == float:
            return price
        else:
            try:
                return float(price)
            except:
                print(price)
                return 0

    @staticmethod
    def get_uchItem(article, uchList: list):
        for item in uchList:
            if article == item.article:
                return item
        ui = unloadedCheescakeItem.UnloadedCheescakeItem()
        return ui
