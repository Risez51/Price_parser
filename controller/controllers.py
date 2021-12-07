from model import resultCreater, fileReader, viewData, parser, viewData
import wx
from view import myWindow

class Controllers(object):


    def __init__(self, app):
        self.frame = myWindow.MyWindow(None, "Прайс_парсер_1.0")
        self.frame.Center()
        self.frame.Show()
        self.view_data = viewData.ViewData()
        self.path_list = ""

        # Binds
        self.frame.Bind(wx.EVT_BUTTON, self.add_cheescake_preport, self.frame.buttonOpenCheesCakeFile)
        self.frame.Bind(wx.EVT_BUTTON, self.add_comparision_report, self.frame.buttonOpenComparisionFile)
        self.frame.Bind(wx.EVT_BUTTON, self.add_supplier_files, self.frame.buttonOpenSupplierPrices)

        self.frame.Bind(wx.EVT_BUTTON, self.del_ulc_row, self.frame.buttonDeleteRow)
        self.frame.Bind(wx.EVT_BUTTON, self.clearULC, self.frame.buttonClearAllUlc)
        self.frame.Bind(wx.EVT_BUTTON, self.start_parse, self.frame.buttonParse)


    def add_cheescake_preport(self, event):
        with self.open_file_dialog() as ofd:
            self.view_data.cheescake_report = {"Отчет чизкейк": ofd.GetPath()}
            self.frame.input_CheesCake.LabelText = ofd.GetFilename()


    def add_comparision_report(self, event):
        with self.open_file_dialog() as ofd:
            self.view_data.comparision_file = {"Таблица соответствий": ofd.GetPath()}
            self.frame.input_comparision.LabelText = ofd.GetFilename()

    def add_supplier_files(self, event):
        dlg = self.open_files_dialog()
        self.add_ulc_items(dlg)
        self.path_list = list(dlg.GetPaths())



    def add_ulc_items(self, dlg):
        file_names = dlg.GetFilenames()
        for i in range(0, len(file_names)):
            self.frame.ulc.InsertStringItem(i, file_names[i])
            self.frame.ulc.SetItemWindow(i, 1, self.create_combobox_ulc())

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
        if dlg.ShowModal() == wx.ID_OK:
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
        if dlg.ShowModal() == wx.ID_OK:
            return dlg
        dlg.Destroy()


    def start_parse(self, event):
        print(self.path_list)
        my_parser = parser.Parser()
        uchList = my_parser.get_products_list(self.view_data.cheescake_report)
        complist = my_parser.get_products_list(self.view_data.comparision_file)
        supplierLists = self.get_suppliers_list()
        rs = resultCreater.ResultCreater(supplierLists, uchList, complist).createResultList()
        self.export_to_excel(rs)


    def get_suppliers_list(self):
        supplierLists = []
        my_parser = parser.Parser()
        for i in range(0, self.frame.ulc.GetItemCount()):
            file_name = self.frame.ulc.GetItemText(i)
            combobox = self.frame.ulc.GetItemWindow(i, 1)
            sup_name = combobox.GetString(combobox.GetSelection())
            if sup_name == "":
                self.validatingUltimateList()
                break
            supplierLists.append(my_parser.get_products_list({sup_name: self.get_path_by_file_name(file_name)}))
        return supplierLists


    def get_path_by_file_name(self, file_name):
        for i in range(len(self.path_list)):
            if file_name in self.path_list[i]:
                return self.path_list[i]
        return ""

    def validatingUltimateList(self):
        dlg = wx.MessageDialog(self, "Не выбран поставщик у одного из файлов", "Ошибка", wx.OK)
        dlg.ShowModal()

    def export_to_excel(self, my_data):
        fileReader.FileReader().to_excel(my_data)
