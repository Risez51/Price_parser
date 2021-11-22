class ResultCreater:
    def __init__(self, listWithsupplierLists, uchList, comparisionList ):
        self.listWithsupplierLists = listWithsupplierLists
        self.uchList = uchList
        self.comparisionList = comparisionList
        pass

    def getCheescakeResult(self):
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
                               "Холдинг, дата размещения": uchItem.orderDate})


    def get_uchItem(self, article, uchList: list):
        for item in uchList:
            if article == item.article:
                return item



    def getResultFromSupplierLists(self, supLists: list):
        resultList = []
        for supList in supLists:
            for supplierProduct in supList:
                resultList.append({f'{supList.keys()}, артикул': supplierProduct.article,
                                   f'{supList.keys()}, цена': supplierProduct.price})






