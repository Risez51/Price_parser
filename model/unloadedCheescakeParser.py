from model import unloadedCheescakeItem, fileWorker, config


class UnloadedCheescakeParser:

    def __init__(self):
        self.fr = fileWorker.FileReader()

    def get_products_list(self, path_to_file):
        result_list = []
        index = config.Config().get_cheescake_indexes()
        file_data = fileWorker.FileReader().get_data_list(path_to_file)
        for row in file_data:
            uchItem = unloadedCheescakeItem.UnloadedCheescakeItem()
            uchItem.article = str(row[index.article]).strip()
            uchItem.name = row[index.name]
            uchItem.purchase_price = self.nan_to_zero(row[index.purchase_price])
            uchItem.supplier_name = row[index.supplier_name]
            uchItem.order_date = row[index.order_date].date()
            uchItem.stock = row[index.stock]
            uchItem.selling_price = self.nan_to_zero(row[index.selling_price])
            uchItem.group = row[index.group]
            result_list.append(uchItem)
        return result_list

    def nan_to_zero(self, value):
        return '0' if str(value) == 'nan' or str(value) == '' else str(value)

