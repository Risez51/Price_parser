from controllers import inputBuilder, ulcBuilder, fileDialogBuilder
from model import viewItems


# Класс управления ULC виджетом в приложение
class FormBuilder:
    def __init__(self, frame, view_items):
        self.view_items = viewItems.ViewItems()
        self.frame = frame
        self.view_items = view_items

        # Обновление полей данных "Отчет чизкейк"

    def append_cheescake_item(self, my_input):
        # file_data = {'имя файла': 'путь к файлу'}
        file_data = fileDialogBuilder.FileDialog(self.frame).open_file()
        # Обновление label инпута "Чизкейк файл" + обновление значения в view_data
        inputBuilder.InputBuilder(self.view_items).update_input_cheescake_label(my_input, file_data)

        # Обновление полей данных "Таблица соответствий"

    def append_comparison_item(self, my_input):
        # file_data = {'имя файла': 'путь к файлу'}
        file_data = fileDialogBuilder.FileDialog(self.frame).open_file()
        # Обновление label инпута "Таблица соответствий" + обновление значения в view_data
        inputBuilder.InputBuilder(self.view_items).update_input_comparison_label(my_input, file_data)

    def append_liquidity_item(self, my_input):
        # file_data = {'имя файла': 'путь к файлу'}
        file_data = fileDialogBuilder.FileDialog(self.frame).open_file()
        # Обновление label инпута "Таблица соответствий" + обновление значения в view_data
        inputBuilder.InputBuilder(self.view_items).update_input_liquidity_label(my_input, file_data)



    def append_ulc_items(self, ulc):
        ulcBuilder.ULCBuilder(ulc, self.view_items).add_ulc_items(fileDialogBuilder.FileDialog(self.frame).open_files())

    def del_ulc_item(self, ulc):
        ulcBuilder.ULCBuilder(ulc, self.view_items).del_selected_item_from_ulc()

    def del_all_ulc_items(self, ulc):
        ulcBuilder.ULCBuilder(ulc, self.view_items).clear_ulc_items()

    def update_view_items_from_ulc(self, ulc):
        ulcBuilder.ULCBuilder(ulc, self.view_items).read_current_data_from_ulc()

    def update_view_items_from_inputs(self):
        inputBuilder.InputBuilder(self.view_items).update_input_items()

    def update_view_items(self, ulc):
        self.view_items.file_tag_path_dict = {}
        self.update_view_items_from_ulc(ulc)
        self.update_view_items_from_inputs()
