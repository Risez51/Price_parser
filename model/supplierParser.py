import pandas as pd
from model import supplierProduct

class SupplierParser():

    def __init__(self, path_to_file: str, article_column: int, price_column: int, sheet=0):
        self.path_to_file = path_to_file
        self.article_column = article_column
        self.price_column = price_column
        self.sheet = sheet

    def getProductListFromXlsx(self):
        product_list = []
        excelFile = pd.ExcelFile(self.path_to_file)
        df = excelFile.parse(sheet_name=self.sheet)
        arr_with_stock_Excel_data = df.to_numpy()

        for item in arr_with_stock_Excel_data:
            if self.isProduct(item[self.article_column],
                              item[self.price_column]):
                product = supplierProduct.SupplierProduct(str(item[self.article_column]).strip(),
                                                          item[self.price_column])
                product_list.append(product)
        return product_list



    def isProduct(self, article, price):
        if len(str(article)) == 0 or article == 0 or str(article) == "nan":
            return False
        if isinstance(price, str) or str(price) == "nan":
            return False
        return True

    def getList(self, listik):
        resultList = []
        for product in listik:
            resultList.append({"артикул": product.article,
                               "цена": product.price})
        return resultList