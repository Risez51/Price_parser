import pandas as pd
import supplierProduct

class SupplierParser():

    def __init__(self, path_to_file: str, article_column: int, price_column: int):
        self.path_to_file = path_to_file
        self.article_column = article_column
        self.price_column = price_column
        self.sheet = 0

    def getProductListFromXlsx(self):
        product_list = []
        #excelFile = pd.ExcelFile(self.path_to_file)
        #df = excelFile.parse(sheet_name=self.sheet)

        df = pd.read_excel(self.path_to_file)
        arr_with_stock_Excel_data = df.to_numpy()

        for item in arr_with_stock_Excel_data:
            if self.isProduct(item[self.article_column],
                              item[self.price_column]):
                product = supplierProduct.SupplierProduct(item[self.article_column],
                                                          item[self.price_column])
                product_list.append(product)
        return product_list

    def isProduct(self, article, price):
        if len(str(article)) == 0 or article == 0 or str(article) == "nan":
            return False
        if isinstance(price, str) or str(price) == "nan":
            return False
        return True