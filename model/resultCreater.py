import pandas as pd
from model import unloadedCheescakeItem


class ResultCreater:
    def __init__(self, listWithsupplierLists, uchList, comparisionList ):
        self.listWithsupplierLists = listWithsupplierLists
        self.uchList = uchList
        self.comparisionList = comparisionList
        pass



    def createResultList(self):
        resultList = []
        for comparisionItem in self.comparisionList:
            uchItem = self.get_uchItem(comparisionItem.holding_article, self.uchList)
            resultList.append({"Холдинг, артикул": comparisionItem.holding_article,
                               "Холдинг, наименование": comparisionItem.name,
                               "Холдинг, группа": comparisionItem.holding_group,
                               "Холдинг, цена закупки": uchItem.purchase_price,
                               "Холдинг, цена продажи": uchItem.selling_price,
                               "Холдинг, остатки": uchItem.stock,
                               "Холдинг, поставщик": uchItem.supplier,
                               "Холдинг, дата размещения": uchItem.orderDate,

                               "Автоключ, артикул": comparisionItem.avtokluch_article,
                               "Автоключ, цена": self.getSupplierParam(self.listWithsupplierLists,
                                                                       "Автоключ",
                                                                       comparisionItem.avtokluch_article),
                               "Автоключ, бренд": comparisionItem.avtokluch_brand,

                               "Дарси 1, артикул": comparisionItem.darsi1_article,
                               "Дарси 1, цена": self.getSupplierParam(self.listWithsupplierLists,
                                                                      "Дарси 1",
                                                                      comparisionItem.darsi1_article),
                               "Дарси 1, разница в цене": self.get_procent_difference(uchItem.selling_price,self.getSupplierParam(self.listWithsupplierLists,
                                                                      "Дарси 1",
                                                                      comparisionItem.darsi1_article)),
                               "Дарси 1, бренд": comparisionItem.darsi1_brand,

                               "Дарси 2, артикул": comparisionItem.darsi2_article,
                               "Дарси 2, цена": self.getSupplierParam(self.listWithsupplierLists,
                                                                      "Дарси 2",
                                                                     comparisionItem.darsi2_article),
                               "Дарси 2, бренд": comparisionItem.darsi2_brand,

                               "Ипц, артикул": comparisionItem.inpo_article,
                               "Ипц, цена": self.getSupplierParam(self.listWithsupplierLists,
                                                                  "Ипц",
                                                                     comparisionItem.inpo_article),
                               "Ипц, бренд": comparisionItem.inpo_brand,

                               "Белый медведь, артикул": comparisionItem.whiteBear_article,
                               "Белый медведь, цена": self.getSupplierParam(self.listWithsupplierLists,
                                                                            "Белый медведь",
                                                                  comparisionItem.whiteBear_article),
                               "Белый медведь, бренд": comparisionItem.whiteBear_brand,

                               "Мир инструментов 1, артикул": comparisionItem.mirInstrumentov1_article,
                               "Мир инструментов 1, цена": self.getSupplierParam(self.listWithsupplierLists,
                                                                                 "Мир инструментов 1",
                                                                            comparisionItem.mirInstrumentov1_article),
                               "Мир инструментов 1, бренд": comparisionItem.mirInstrumentov1_brand,

                               "Мир инструментов 2, артикул": comparisionItem.mirInstrumentov2_article,
                               "Мир инструментов 2, цена": self.getSupplierParam(self.listWithsupplierLists,
                                                                                 "Мир инструментов 2",
                                                                                 comparisionItem.mirInstrumentov2_article),
                               "Мир инструментов 2, бренд": comparisionItem.mirInstrumentov2_brand,
                               })
        return resultList


    def getSupplierParam(self, listWithsupplierLists, supplier, article):
        for supplierList in listWithsupplierLists:
            supKeys = list(supplierList.keys())
            if supKeys[0] == supplier:
                for supplierProduct in supplierList.get(supplier):
                    if str(supplierProduct.article) == article:
                        return supplierProduct.price
        return 0


    def getResultExcelFile(self, resultList):
        df = pd.DataFrame(data=resultList)
        df.to_excel('resultFile.xlsx', index=False)
        print("result file complited")

    def get_procent_difference(self, price_holding, price_supplier):
        p_hold = self.get_float_from_price(price_holding)
        p_sup = self.get_float_from_price(price_supplier)
        one_procent = p_hold / 100
        procent = (p_sup / one_procent) - 100
        return f'{procent:.2f}%'


    def get_float_from_price(self, price):
        if type(price) == int or type(price) == float:
            return price
        else:
            try:
                return float(price)
            except:
                print(price)
                return 0

    def get_uchItem(self, article, uchList: list):
        for item in uchList:
            if article == item.article:
                return item
        ui = unloadedCheescakeItem.UnloadedCheescakeItem()
        return ui