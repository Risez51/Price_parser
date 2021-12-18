from model import supplierProduct


class SupplierParser:
    def __init__(self, excel_data: list, article_column: int, price_column: int):
        self.products_list = []
        self.article_column = article_column
        self.price_column = price_column
        self.excel_data = excel_data

    def get_products_list(self):
        for excel_row in self.excel_data:
            self.append_to_list(excel_row)
        return self.products_list

    def append_to_list(self, excel_row):
        #print(excel_row[self.article_column], excel_row[self.price_column])
        if self.is_product(excel_row[self.article_column],
                           excel_row[self.price_column]):
            self.products_list.append(self.new_product(excel_row[self.article_column],
                                                       excel_row[self.price_column]))

    def new_product(self, article, price):
        return supplierProduct.SupplierProduct(self.fix_str(article), self.fix_str(price))

    @staticmethod
    def fix_str(value):
        return str(value).strip()

    @staticmethod
    def is_product(article, price):
        return str(article) != 'nan' or str(price) != 'nan' or len(str(article)) != 0 or article != 0 or price != 0.0 or price != 0 or str(price) != ''
