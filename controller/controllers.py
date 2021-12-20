from model import config
import wx
from view import myWindow
from controller import formBuilder, viewItems, validator, resultCreater


class Controllers(object):

    def __init__(self, app):
        self.frame = myWindow.MyWindow(None, "Прайс_парсер_1.0")
        self.frame.Center()
        self.frame.Show()
        self.cnfg = config.Config()
        self.view_items = viewItems.ViewItems()
        self.form_builder = formBuilder.FormBuilder(self.frame, self.view_items)
        # Binds
        self.frame.Bind(wx.EVT_MENU, self.onExit, self.frame.exitItem)
        self.frame.Bind(wx.EVT_MENU, self.onAbout, self.frame.aboutItem)

        self.frame.Bind(wx.EVT_BUTTON, self.add_cheescake_report, self.frame.button_cheescake)
        self.frame.Bind(wx.EVT_BUTTON, self.add_comparision_report, self.frame.buttonOpenComparisionFile)
        self.frame.Bind(wx.EVT_BUTTON, self.update_ulc_items, self.frame.buttonOpenSupplierPrices)

        self.frame.Bind(wx.EVT_BUTTON, self.del_focused_ulc_item, self.frame.buttonDeleteRow)
        self.frame.Bind(wx.EVT_BUTTON, self.del_all_ulc_items, self.frame.buttonClearAllUlc)
        self.frame.Bind(wx.EVT_BUTTON, self.start_parsing, self.frame.buttonParse)

    # Добавляет отчет чизкейк на форму
    def add_cheescake_report(self, event):
        self.form_builder.append_cheescake_item(self.frame.input_cheescake)

    # Добавляет таблицу соответствий на форму
    def add_comparision_report(self, event):
        self.form_builder.append_comparison_item(self.frame.input_comparision)

    # Добавление items в ULC
    def update_ulc_items(self, event):
        self.form_builder.append_ulc_items(self.frame.ulc)

    # Удаляет строку со значениями компонента ULC
    def del_focused_ulc_item(self, event):
        self.form_builder.del_ulc_item(self.frame.ulc)

    # Очистка содержимого компонента ULC
    def del_all_ulc_items(self, event):
        self.form_builder.del_all_ulc_items(self.frame.ulc)

    # Старт парсинга - срабатывает, при нажатие на кнопку "Спарсить"
    def start_parsing(self, event):
        self.frame.progress_bar.SetValue(0)
        if validator.ViewValidator(self.frame).is_valid():
            # Обновляет данные с вью формы в view_items
            self.form_builder.update_view_items_from_ulc(self.frame.ulc)
            # создает результирующий файл на 1 листе
            resultCreater.ResultCreator(self.view_items).get_result_excel_file(self.frame.rbox)
            self.frame.progress_bar.SetValue(100)

    def onAbout(self, event):
        dlg = wx.MessageDialog(self.frame,
                               'По вопросам о работе программы пишите: \n  i.rudometkin@instrland.ru',
                               'О программе',
                               wx.OK)
        dlg.ShowModal()

    def onExit(self, event):
        wx.Exit()
