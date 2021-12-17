import configparser


class Config:
    def __init__(self):
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read('settings.ini', encoding='utf-8')
        self.supplier_names = self.get_supplier_names_list()

    # Возвращает список названий всех поставщиков
    def get_supplier_names_list(self):
        return self.config_parser.get('Suppliers', 'names').split(", ")

    # Возвращает №колонки_с_артикулом
    def get_article_column_index(self, supplier_name):
        return int(self.config_parser.get('Column_article', supplier_name))

    # Возвращает №колонки_с_ценой
    def get_price_column_index(self, supplier_name):
        return int(self.config_parser.get('Column_price', supplier_name))

    def get_comparison_column_index(self, name):
        return int(self.config_parser.get('Comparison_column', name))
