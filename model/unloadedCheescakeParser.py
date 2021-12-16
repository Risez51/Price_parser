import pandas as pd
from model import unloadedCheescakeItem, fileReader


class UnloadedCheescakeParser:

    def __init__(self):
        self.fr = fileReader.FileReader()
        pass

    def get_products_list(self, path_to_file):
        result_list = []
        for item in self.fr.get_data_list(path_to_file):
            uchItem = unloadedCheescakeItem.UnloadedCheescakeItem()
            uchItem.article = str(item[0]).strip()
            uchItem.name = item[1]
            uchItem.purchase_price = item[2]
            uchItem.supplier = item[4]
            uchItem.orderDate = item[5].date()
            uchItem.stock = item[6]
            uchItem.selling_price = item[7]
            uchItem.group = item[8]
            result_list.append(uchItem)
        return result_list