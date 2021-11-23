import comparisionItem
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
            compItem.holding_article = str(item[1]).strip()
            compItem.holding_group = item[2]
            compItem.avtokluch_brand = item[4]
            compItem.avtokluch_article = str(item[5]).strip()
            compItem.darsi1_brand = item[7]
            compItem.darsi1_article = str(item[8]).strip()
            compItem.darsi2_brand = item[10]
            compItem.darsi2_article = str(item[11]).strip()
            compItem.inpo_brand = item[13]
            compItem.inpo_article = str(item[14]).strip()
            compItem.whiteBear_brand = item[16]
            compItem.whiteBear_article = str(item[17]).strip()
            compItem.mirInstrumentov1_brand = item[19]
            compItem.mirInstrumentov1_article = str(item[20]).strip()
            compItem.mirInstrumentov2_brand = item[22]
            compItem.mirInstrumentov2_article = str(item[23]).strip()
            comparisionList.append(compItem)
        return comparisionList

    def getComparasionList(self, compList):
        pass