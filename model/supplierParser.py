from model import supplierProduct

class SupplierParser:
    def __init__(self, my_data: list, article_column: int, price_column: int):
        self.products_list = []
        self.article_column = article_column
        self.price_column = price_column
        self.my_data = my_data

    def get_products_list(self):
        for item in self.my_data:
            self.append_to_list(item)
        return self.products_list

    def append_to_list(self, item):
        if self.is_product(item[self.article_column],
                           item[self.price_column]):
            self.products_list.append(self.new_product(item[self.article_column],
                                                       item[self.price_column]))

    def new_product(self, article, price):
        return supplierProduct.SupplierProduct(self.fix_str(article), price)

    def fix_str(self, value):
        return str(value).strip()

    def is_product(self, article, price):
        if str(article) == "nan" or str(price) == "nan" or len(str(article)) == 0 or article == 0:
            return False
        else:
            return True
