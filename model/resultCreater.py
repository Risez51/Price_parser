from model import parser, productsComposer, fileWorker
import sys


class ResultCreator:
    def __init__(self, view_items):
        self.view_items = view_items
        self.my_parser = parser.Parser()
        self.all_files_dict = {}
        self.get_result_dict()

    def get_result_excel_file(self, radio_box):
        if radio_box.GetString(radio_box.GetSelection()) == 'В 1 файл':
            self.get_result_on_one_excel_sheet()
        elif radio_box.GetString(radio_box.GetSelection()) == 'По группам':
            self.get_result_on_several_excel_sheets()



    # По итогу создает result_file с группами в 1 листе
    def get_result_on_one_excel_sheet(self):
        result = productsComposer.ProductsComposer(self.all_files_dict).create_result_for_one_sheet()
        fileWorker.FileWriter().to_excel_on_one_sheet(result)

    def get_result_on_several_excel_sheets(self):
        result = productsComposer.ProductsComposer(self.all_files_dict).create_result_for_several_sheets()
        fileWorker.FileWriter().to_excel_on_several_sheets(result)

    def get_result_dict(self):
        for file_tag in self.view_items.file_tag_path_dict:
            try:
                self.all_files_dict.update(
                    self.my_parser.get_products_list({file_tag: self.view_items.file_tag_path_dict.get(file_tag)}))
            except:
                print(f'{file_tag}: некорректный формат')
                sys.exit()
