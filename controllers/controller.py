from model import resultCreater, viewItems
import wx
from view import myWindow
from controllers import formBuilder, validator


class Controller(object):

    def __init__(self, app):
        self.frame = myWindow.MyWindow(None, "Прайс_парсер_1.0")
        self.frame.Center()
        self.frame.Show()
        self.view_items = viewItems.ViewItems()
        self.form_builder = formBuilder.FormBuilder(self.frame, self.view_items)
        # Binds
        self.frame.Bind(wx.EVT_MENU, self.onExit, self.frame.exitItem)
        self.frame.Bind(wx.EVT_MENU, self.onAbout, self.frame.aboutItem)

        self.frame.Bind(wx.EVT_BUTTON, self.add_cheescake_report, self.frame.button_cheescake)
        self.frame.Bind(wx.EVT_BUTTON, self.add_comparison_report, self.frame.buttonOpenComparisionFile)
        self.frame.Bind(wx.EVT_BUTTON, self.add_liquidity_report, self.frame.buttonOpenLiquidityFile)
        self.frame.Bind(wx.EVT_BUTTON, self.update_ulc_items, self.frame.buttonOpenSupplierPrices)
        self.frame.Bind(wx.EVT_RADIOBOX, self.update_radiogroup_value, self.frame.rbox)
        self.frame.Bind(wx.EVT_BUTTON, self.test_button, self.frame.buttonTest)
        self.view_items.radiogroup_value = self.frame.rbox.GetString(self.frame.rbox.GetSelection())

        self.frame.Bind(wx.EVT_BUTTON, self.del_focused_ulc_item, self.frame.buttonDeleteRow)
        self.frame.Bind(wx.EVT_BUTTON, self.del_all_ulc_items, self.frame.buttonClearAllUlc)
        self.frame.Bind(wx.EVT_BUTTON, self.start_parsing, self.frame.buttonParse)


    def test_button(self, event):
        print(f'view_item.radiogroup_value: {self.view_items.radiogroup_value}')

    # Обновляет значение указанное в радиогруппе
    def update_radiogroup_value(self, event):
        self.form_builder.update_view_item_from_radiogroup(self.frame.rbox)

    # Добавляет отчет чизкейк на форму
    def add_cheescake_report(self, event):
        self.form_builder.append_cheescake_item(self.frame.input_cheescake)

    # Добавляет таблицу соответствий на форму
    def add_comparison_report(self, event):
        self.form_builder.append_comparison_item(self.frame.input_comparision)

    def add_liquidity_report(self, event):
        self.form_builder.append_liquidity_item(self.frame.input_liquidity)

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
        # Если все необходимые файлы добавлены на форму
        if validator.ViewValidator(self.frame).is_valid():
            # Обновляет данные с вью формы в view_items
            self.form_builder.update_view_items(self.frame.ulc)
            # создает результирующий файл
            resultCreater.ResultCreator(self.view_items).create_result_excel_file()
            self.frame.progress_bar.SetValue(100)

    def onAbout(self, event):
        dlg = wx.MessageDialog(self.frame,
                               'По вопросам о работе программы пишите: \n  i.rudometkin@instrland.ru',
                               'О программе',
                               wx.OK)
        dlg.ShowModal()

    def onExit(self, event):
        wx.Exit()
