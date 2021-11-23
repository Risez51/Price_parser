import pandas as pd

import unloadedCheescakeItem


class UnloadedCheescakeParser():

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def getUnloadedCheescakeList(self):
        comparisionList = []
        excelFile = pd.ExcelFile(self.path_to_file)
        df = excelFile.parse()
        arr_with_stock_Excel_data = df.to_numpy()
        resList = []
        for item in arr_with_stock_Excel_data:
            ichItem = unloadedCheescakeItem.UnloadedCheescakeItem()
            ichItem.article = str(item[0]).strip()
            ichItem.name = item[1]
            ichItem.purchase_price = item[2]
            ichItem.supplier = item[3]
            ichItem.orderDate = item[4]
            ichItem.stock = item[5]
            ichItem.selling_price = item[6]
            ichItem.group = item[7]
            resList.append(ichItem)
        return resList