import pandas as pd
from model import unloadedCheescakeItem, fileReader


class UnloadedCheescakeParser:

    def __init__(self):
        self.fr = fileReader.FileReader()
        pass

    def get_products_list(self, path_to_file):
        result_list = []
        for item in self.fr.get_data_list(path_to_file):
            ichItem = unloadedCheescakeItem.UnloadedCheescakeItem()
            ichItem.article = str(item[0]).strip()
            ichItem.name = item[1]
            ichItem.purchase_price = item[2]
            ichItem.supplier = item[4]
            ichItem.orderDate = item[5].date()
            ichItem.stock = item[6]
            ichItem.selling_price = item[7]
            ichItem.group = item[8]
            result_list.append(ichItem)
        return result_list