from model import comparisionItem, fileWorker


class ComparisionParser:

    def __init__(self):
        self.file_reader = fileWorker.FileReader()

    def get_products_list(self, path_to_file):
        comparisionList = []
        for item in self.file_reader.get_data_list(path_to_file):
            compItem = comparisionItem.ComparisionItem()
            compItem.holding_name = item[1]
            compItem.holding_article = self.fix_str(item[0])
            compItem.holding_group = item[3]

        return comparisionList

    #Обрезает пробелы слева и справа
    @staticmethod
    def fix_str(value):
        return str(value).strip()

    # Артикул в прайсе поставщика имеет длину 6 (ноли перед артикулом, например 000001), в таблице соответствий
    # данный артикул хранится со значением 1 - функция дополняет артикул нолями.
    def fix_kem_article(self, article):
        if article != "nan" or article != "0" or article != "":
            article = str(article).replace(".0", "")
            while len(article) < 6:
                article = "0" + article
            return article