from model import comparisionParser, supplierParser, unloadedCheescakeParser, fileReader


class Parser:

    def __init__(self):
        self.fr = fileReader.FileReader()

    def choose_file_parser(self,  file_tag, file_path):
        if file_tag == "Отчет чизкейк":
            return {file_tag: unloadedCheescakeParser.UnloadedCheescakeParser().get_products_list(file_path)}
        elif file_tag == "Таблица соответствий":
            return {file_tag: comparisionParser.ComparisionParser().get_products_list(file_path)}
        elif file_tag == "Дарси":
            return {file_tag: self.parse_supplier(file_path, 2, 4)}
        elif file_tag == "Мир инструментов":
            return {file_tag: self.parse_supplier(file_path, 0, 8)}
        elif file_tag == "Белый медведь":
            return {file_tag: self.parse_supplier(file_path, 1, 3)}
        elif file_tag == "Автоключ":
            return {file_tag: self.parse_supplier(file_path, 0, 7)}
        elif file_tag == "Ипц":
            return {file_tag: self.parse_supplier(file_path, 0, 2)}
        else:
            return []

    def get_products_list(self, dic):
        keys = list(dic.keys())[0]
        values = list(dic.values())[0]
        return self.choose_file_parser(str(keys), str(values))



    def parse_supplier(self, file_path, article_column, price_column):
        return supplierParser.SupplierParser(self.fr.get_data_list(file_path),
                                             article_column, price_column).get_products_list()
