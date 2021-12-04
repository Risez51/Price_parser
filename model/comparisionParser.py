from model import comparisionItem, fileReader


class ComparisionParser:

    def __init__(self):
        self.fr = fileReader.FileReader()
        pass

    def get_products_list(self, path_to_file):
        comparisionList = []
        for item in self.fr.get_data_list(path_to_file):
            compItem = comparisionItem.ComparisionItem()
            compItem.name = item[0]
            compItem.holding_article = self.fix_str(item[1])
            compItem.holding_group = item[2]
            compItem.avtokluch_brand = item[4]
            compItem.avtokluch_article = self.fix_str(item[5])
            compItem.darsi1_brand = item[7]
            compItem.darsi1_article = self.fix_str(item[8])
            compItem.darsi2_brand = item[10]
            compItem.darsi2_article = self.fix_str(item[11])
            compItem.inpo_brand = item[13]
            compItem.inpo_article = self.fix_str(item[14])
            compItem.whiteBear_brand = item[16]
            compItem.whiteBear_article = self.fix_str(item[17])
            compItem.mirInstrumentov1_brand = item[19]
            compItem.mirInstrumentov1_article = self.fix_str(item[20])
            compItem.mirInstrumentov2_brand = item[22]
            compItem.mirInstrumentov2_article = self.fix_str(item[23])
            comparisionList.append(compItem)
        return comparisionList

    def fix_str(self, value):
        return str(value).strip()
