from model import comparisionParser, supplierParser, unloadedCheescakeParser, fileWorker, productsComposer, config


class Parser:

    def __init__(self):
        self.fr = fileWorker.FileReader()

    def choose_file_parser(self,  file_tag, file_path):
        conf = config.Config()

        if file_tag == conf.cheescake_report_name():
            return {file_tag: unloadedCheescakeParser.UnloadedCheescakeParser().get_products_list(file_path)}
        elif file_tag == conf.comparison_report_name():
            return {file_tag: comparisionParser.ComparisionParser().get_products_list(file_path)}
        else:
            return {file_tag: self.parse_supplier(file_path,
                                                  conf.get_article_column_index(file_tag),
                                                  conf.get_price_column_index(file_tag))}

    #Вход: словарь {имя_поставщика: путь к файлу}
    def get_products_list(self, dictionary):
        for file_tag in dictionary:
            return self.choose_file_parser(str(file_tag), str(dictionary.get(file_tag)))

    def get_result_data(self, data):
        return productsComposer.ProductsComposer(data).create_result()

    def parse_supplier(self, file_path, article_column, price_column):
        return supplierParser.SupplierParser(self.fr.get_data_list(file_path),
                                             article_column, price_column).get_products_list()
