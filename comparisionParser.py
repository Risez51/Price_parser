import comparisionItem
import supplierProduct
import pandas as pd
class ComparisionParser():

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def getComparisionList(self):
        comparisionList = []
        excelFile = pd.ExcelFile(self.path_to_file)
        df = excelFile.parse()
        arr_with_stock_Excel_data = df.to_numpy()
        for item in arr_with_stock_Excel_data:
            compItem = comparisionItem.ComparisionItem()
            compItem.name = item[0]
            compItem.holding_article = item[1]
            compItem.holding_group = item[2]
            compItem.avtokluch_brand = item[4]
            compItem.avtokluch_article = item[5]
            compItem.darsi1_brand = item[7]
            compItem.darsi1_article = item[8]
            compItem.darsi2_brand = item[10]
            compItem.darsi2_article = item[11]
            compItem.inpo_brand = item[13]
            compItem.inpo_article = item[14]
            compItem.whiteBear_brand = item[16]
            compItem.whiteBear_article = item[17]
            compItem.mirInstrumentov1_brand = item[19]
            compItem.mirInstrumentov1_article = item[20]
            compItem.mirInstrumentov2_brand = item[22]
            compItem.mirInstrumentov2_article = item[23]
            comparisionList.append(compItem)
        return comparisionList