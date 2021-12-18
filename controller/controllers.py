import sys
from model import fileWorker, parser, viewData, config
import wx
from view import myWindow
from controller import formBuilder, viewItems


class Controllers(object):

    def __init__(self, app):
        self.frame = myWindow.MyWindow(None, "Прайс_парсер_1.0")
        self.frame.Center()
        self.frame.Show()
        self.cnfg = config.Config()
        self.view_data = viewData.ViewData()
        self.view_items = viewItems.ViewItems()
        self.path_list = []
        self.all_files_dict = {}
        self.form_builder = formBuilder.FormBuilder(self.frame, self.view_items)
        # Binds
        self.frame.Bind(wx.EVT_MENU, self.onExit, self.frame.exitItem)
        self.frame.Bind(wx.EVT_MENU, self.onAbout, self.frame.aboutItem)

        self.frame.Bind(wx.EVT_BUTTON, self.add_cheescake_report, self.frame.button_cheescake)
        self.frame.Bind(wx.EVT_BUTTON, self.add_comparision_report, self.frame.buttonOpenComparisionFile)
        self.frame.Bind(wx.EVT_BUTTON, self.update_ulc_items, self.frame.buttonOpenSupplierPrices)

        self.frame.Bind(wx.EVT_BUTTON, self.del_focused_ulc_row, self.frame.buttonDeleteRow)
        self.frame.Bind(wx.EVT_BUTTON, self.clear_ulc_items, self.frame.buttonClearAllUlc)
        self.frame.Bind(wx.EVT_BUTTON, self.start_parsing, self.frame.buttonParse)

    # Добавляет отчет чизкейк на форму
    def add_cheescake_report(self, event):
        self.form_builder.append_cheescake_item(self.frame.input_cheescake)

    # Добавляет таблицу соответствий на форму
    def add_comparision_report(self, event):
        self.form_builder.append_comparison_item(self.frame.input_comparision)

    #Добавление items в ULC
    def update_ulc_items(self, event):
        self.form_builder.append_ulc_items(self.frame.ulc)

    # Удаляет строку со значениями компонента ULC
    def del_focused_ulc_row(self, event):
        self.form_builder.del_ulc_item(self.frame.ulc)

    # Очистка содержимого компонента ULC
    def clear_ulc_items(self, event):
        self.form_builder.del_all_ulc_items(self.frame.ulc)

    # Старт парсинга - срабатывает, при нажатие на кнопку "Спарсить"
    def start_parsing(self, event):
        if self.validating_frame_data():
            self.get_suppliers_list()
            self.frame.progress_bar.SetValue(100)

    # Возвращает словарь {supplier_name: путь к файлу}, где supplier_name - то, что выбрал юзер в combobox
    def get_suppliers_list(self):
        my_parser = parser.Parser()

        #Обновление данных с ulc в view_items
        self.form_builder.update_data_from_ulc(self.frame.ulc)
        for file_tag in self.view_items.file_tag_path_dict:
            try:
                self.all_files_dict.update(
                my_parser.get_products_list({file_tag: self.view_items.file_tag_path_dict.get(file_tag)}))
            except:
                self.error_message(f'{file_tag}: некорректный формат')
                sys.exit()
        self.export_to_excel(my_parser.get_result_data(self.all_files_dict))

    # Валидация заполненности визуальной формы
    def validating_frame_data(self):
        if self.frame.input_cheescake.LabelText == '':
            self.error_message('Отсутствует отчет чизкейк')
            return False
        elif self.frame.input_comparision.LabelText == "":
            self.error_message('Отсутствует таблица соответствий')
            return False
        for i in range(0, self.frame.ulc.GetItemCount()):
            combobox = self.frame.ulc.GetItemWindow(i, 1)
            sup_name = combobox.GetString(combobox.GetSelection())
            if sup_name == '':
                self.error_message(f'Не выбран поставщик для файла: {self.frame.ulc.GetItemText(i)}')
                return False
        return True

    def error_message(self, text):
        dlg = wx.MessageDialog(self.frame, f'{text}', 'Ошибка', wx.OK)
        dlg.ShowModal()

    def export_to_excel(self, my_data):
        fileWorker.FileWriter().to_excel(my_data)

    def onAbout(self, event):
        dlg = wx.MessageDialog(self.frame,
                               'По вопросам о работе программы пишите: \n  i.rudometkin@instrland.ru',
                               'О программе',
                               wx.OK)
        dlg.ShowModal()

    def onExit(self, event):
        wx.Exit()
        pass