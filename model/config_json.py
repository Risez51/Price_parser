import json
from model import supplierProduct, unloadedCheescakeItem


class ConfigJson:
    def __init__(self):
        with open('configs.json', 'r', encoding='utf-8') as reader:
            self.json_file = json.load(reader)

    # Возвращает список всех имеющихся поставщиков в configs.json
    def get_supplier_names_list(self):
        return [supplier_item_dict.get('supplier_name') for supplier_item_dict in self.json_file['Suppliers']]

    # Возвращает supplierProduct, где article = индекс_столбца_с_артикулом, price - индекс_столбца_с_ценой
    def get_indices_for_parse_by_supplier_name(self, supplier_name):
        return [supplierProduct.SupplierProduct(supplier_item_dict.get('article_column'),
                                                supplier_item_dict.get('price_column'))
                for supplier_item_dict in self.json_file['Suppliers']
                if supplier_item_dict.get('supplier_name') == supplier_name][0]

    # Возвращает unloadedCheescakeItem, где поля = индексу
    def get_indices_for_parse_cheescake_report(self):
        uch_item = unloadedCheescakeItem.UnloadedCheescakeItem()
        for item in self.json_file['Отчет чизкейк']:
            uch_item.article = item.get('article_index')
            uch_item.name = item.get('name_index')
            uch_item.supplier_name = item.get('supplier_name_index')
            uch_item.purchase_price = item.get('purchase_price_index')
            uch_item.selling_price = item.get('selling_price_index')
            uch_item.stock = item.get('stock_index')
            uch_item.order_date = item.get('order_date_index')
            uch_item.group = item.get('group_index')
        return uch_item

    def get_indices_comparison_by_name(self, name):
        result = []
        for supplier_indices_dict in self.json_file['Таблица соответствий']:
            if supplier_indices_dict.get('supplier_name') == name:
                article_columns = supplier_indices_dict.get('article_column_indices')
                brand_columns = supplier_indices_dict.get('brand_column_indices')
                for i in range(len(article_columns)):
                    result.append({article_columns[i], brand_columns[i]})
        return result

    def get_cheescake_report_name(self):
        for file_name in self.json_file['Report_names']:
            if file_name.get('cheescake_report'):
                return file_name.get('cheescake_report')

    def get_comparison_report_name(self):
        for file_name in self.json_file['Report_names']:
            if file_name.get('comparison_report'):
                return file_name.get('comparison_report')



