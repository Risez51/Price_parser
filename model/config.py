import configparser
from model import unloadedCheescakeItem


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

    # Возвращает номер колонки в таблице соответствий
    def get_comparison_column_index(self, name):
        return int(self.config_parser.get('Comparison_column', name))

    def get_cheescake_report_name(self):
        return str(self.config_parser.get('Reports', 'cheescake_report'))

    def get_comparison_report_name(self):
        return str(self.config_parser.get('Reports', 'comparison_report'))

    def get_liquidity_report_name(self):
        return str(self.config_parser.get('Reports', 'liquidity_report'))



    def get_cheescake_indexes(self):
        uch_indexes = unloadedCheescakeItem.UnloadedCheescakeItem()
        uch_indexes.article = int(self.config_parser.get('Cheescake_columns', 'article'))
        uch_indexes.name = int(self.config_parser.get('Cheescake_columns', 'name'))
        uch_indexes.supplier_name = int(self.config_parser.get('Cheescake_columns', 'supplier_name'))
        uch_indexes.purchase_price = int(self.config_parser.get('Cheescake_columns', 'purchase_price'))
        uch_indexes.selling_price = int(self.config_parser.get('Cheescake_columns', 'selling_price'))
        uch_indexes.stock = int(self.config_parser.get('Cheescake_columns', 'stock'))
        uch_indexes.order_date = int(self.config_parser.get('Cheescake_columns', 'order_date'))
        uch_indexes.group = int(self.config_parser.get('Cheescake_columns', 'group'))
        return uch_indexes

