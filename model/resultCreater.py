from model import parser, productsComposer, fileWorker
import sys


class ResultCreator:
    def __init__(self, view_items):
        self.view_items = view_items
        self.my_parser = parser.Parser()

    def create_result_excel_file(self, radio_box):
        if radio_box.GetString(radio_box.GetSelection()) == 'В 1 файл':
            self.get_result_on_one_excel_sheet()
        elif radio_box.GetString(radio_box.GetSelection()) == 'По группам':
            self.get_result_on_several_excel_sheets()

    # Cоздает result_file с группами в 1 листе
    def get_result_on_one_excel_sheet(self):
        result = productsComposer.ProductsComposer(self.get_result_dict()).create_result_for_one_sheet()
        fileWorker.FileWriter().to_excel_on_one_sheet(result)

    # Cоздает result_file с группами в разных листах
    def get_result_on_several_excel_sheets(self):
        result = productsComposer.ProductsComposer(self.get_result_dict()).create_result_for_several_sheets()
        fileWorker.FileWriter().to_excel_on_several_sheets(result)

    # Возвращает словарь {file_tag: parsed_products_list, ..., n}
    def get_result_dict(self):
        result_dict = {}
        for file_tag in self.view_items.file_tag_path_dict:
            try:
                result_dict.update(
                    self.my_parser.get_products_list({file_tag: self.view_items.file_tag_path_dict.get(file_tag)}))
            except:
                print(f'{file_tag}: некорректный формат')
                sys.exit()
        return result_dict

