import sys

from model import fileReader, parser, viewData
import wx
from wx.lib.agw import ultimatelistctrl as ULC
from view import myWindow


class Controllers(object):

    def __init__(self, app):
        self.frame = myWindow.MyWindow(None, "Прайс_парсер_1.0")
        self.frame.Center()
        self.frame.Show()
        self.view_data = viewData.ViewData()
        self.path_list = []
        self.all_files_dict = {}

        # Binds
        self.frame.Bind(wx.EVT_MENU, self.onExit, self.frame.exitItem)
        self.frame.Bind(wx.EVT_MENU, self.onAbout, self.frame.aboutItem)

        self.frame.Bind(wx.EVT_BUTTON, self.add_cheescake_preport, self.frame.buttonOpenCheesCakeFile)
        self.frame.Bind(wx.EVT_BUTTON, self.add_comparision_report, self.frame.buttonOpenComparisionFile)
        self.frame.Bind(wx.EVT_BUTTON, self.add_supplier_files, self.frame.buttonOpenSupplierPrices)

        self.frame.Bind(wx.EVT_BUTTON, self.del_ulc_row, self.frame.buttonDeleteRow)
        self.frame.Bind(wx.EVT_BUTTON, self.clearULC, self.frame.buttonClearAllUlc)
        self.frame.Bind(wx.EVT_BUTTON, self.start_parse, self.frame.buttonParse)

    def add_cheescake_preport(self, event):
        with self.open_file_dialog() as ofd:
            self.all_files_dict["Отчет чизкейк"] = ofd.GetPath()
            self.frame.input_CheesCake.LabelText = ofd.GetFilename()

    def add_comparision_report(self, event):
        with self.open_file_dialog() as ofd:
            self.all_files_dict["Таблица соответствий"] = ofd.GetPath()
            self.frame.input_comparision.LabelText = ofd.GetFilename()

    def add_supplier_files(self, event):
        with self.open_files_dialog() as dlg:
            self.add_ulc_items(dlg)
            self.path_list += list(dlg.GetPaths())

    def add_ulc_items(self, dlg):
        file_names = dlg.GetFilenames()
        for i in range(0, len(file_names)):
            self.frame.ulc.InsertStringItem(i, file_names[i])
            self.frame.ulc.SetItemWindow(i, 1, self.create_combobox_ulc(), ULC.ULC_ALIGN_LEFT)

    def create_combobox_ulc(self):
        combobox = wx.Choice(self.frame.ulc)
        combobox.AppendItems(self.view_data.all_supplier_list)
        combobox.Bind(wx.EVT_MOUSEWHEEL, self.doNothing)
        return combobox

    def doNothing(self, event):
        pass

    def open_files_dialog(self):
        dlg = wx.FileDialog(
            self.frame, message="Добавить файлы...",
            defaultDir=".",
            defaultFile="", wildcard="*.xls; *.xlsx; *.csv", style=wx.FD_MULTIPLE)
        if dlg.ShowModal() == wx.ID_OK or wx.ID_EXIT:
            return dlg
        dlg.Destroy()

    def del_ulc_row(self, event):
        if self.frame.ulc.GetFocusedItem() > -1:
            self.frame.ulc.DeleteItem(self.frame.ulc.GetFocusedItem())

    def clearULC(self, event):
        self.frame.ulc.DeleteAllItems()
        self.view_data.supplierFiles = ""

    def open_file_dialog(self):
        dlg = wx.FileDialog(
            self.frame, message="Добавить файл...",
            defaultDir=".",
            defaultFile="", wildcard="*.xls; *.xlsx; *.csv", style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK or wx.ID_EXIT:
            return dlg
        dlg.Destroy()

    def start_parse(self, event):
        if self.validating_frame_data():
            self.frame.progress_bar.SetValue(20)
            self.get_suppliers_list()
            self.frame.progress_bar.SetValue(100)

    def get_suppliers_list(self):
        my_parser = parser.Parser()
        try:
            self.all_files_dict.update(
            my_parser.get_products_list({"Отчет чизкейк": self.all_files_dict.get("Отчет чизкейк")}))
        except:
            self.error_message("Отчет чизкейк: некорректный формат")
            sys.exit()
        try:
            self.all_files_dict.update(
            my_parser.get_products_list({"Таблица соответствий": self.all_files_dict.get("Таблица соответствий")}))
        except:
            self.error_message("Таблица соответствий: некорректный формат")
            sys.exit()
        for i in range(0, self.frame.ulc.GetItemCount()):
            file_name = self.frame.ulc.GetItemText(i)
            sup_name = self.frame.ulc.GetItemWindow(i, 1).GetString(self.frame.ulc.GetItemWindow(i, 1).GetSelection())
            try:
                self.all_files_dict.update(
                my_parser.get_products_list({f'{sup_name}': self.get_path_by_file_name(file_name)}))
            except:
                self.error_message(f"{file_name}: некорректный формат ")
                sys.exit()
        self.export_to_excel(my_parser.get_result_data(self.all_files_dict))


    def validating_frame_data(self):
        if self.frame.input_CheesCake.LabelText == "":
            self.error_message("Отсутствует отчет чизкейк")
            return False
        elif self.frame.input_comparision.LabelText == "":
            self.error_message("Отсутствует таблица соответствий")
            return False
        for i in range(0, self.frame.ulc.GetItemCount()):
            combobox = self.frame.ulc.GetItemWindow(i, 1)
            sup_name = combobox.GetString(combobox.GetSelection())
            if sup_name == "":
                self.error_message(f"Не выбран поставщик для файла: {self.frame.ulc.GetItemText(i)}")
                return False
        return True

    def get_path_by_file_name(self, file_name):
        for i in range(len(self.path_list)):
            if file_name in self.path_list[i]:
                return self.path_list[i]
        return ""

    def error_message(self, text):
        dlg = wx.MessageDialog(self.frame, f"{text}", "Ошибка", wx.OK)
        dlg.ShowModal()

    def export_to_excel(self, my_data):
        fileReader.FileReader().to_excel(my_data)

    def onAbout(self, event):
        dlg = wx.MessageDialog(self.frame, "По вопросам о работе программы пишите: \n  i.rudometkin@instrland.ru", "О программе", wx.OK)
        dlg.ShowModal()

    def onExit(self, event):
        wx.Exit()
        pass