from model import resultCreater, fileReader, viewData, parser, viewData
import wx
from view import myWindow

class Controllers(object):


    def __init__(self, app):
        self.frame = myWindow.MyWindow(None, "Прайс_парсер_1.0")
        self.frame.Center()
        self.frame.Show()
        self.view_data = viewData.ViewData()
        self.all_files_list = []

        # Binds
        self.frame.Bind(wx.EVT_BUTTON, self.add_cheescake_preport, self.frame.buttonOpenCheesCakeFile)
        self.frame.Bind(wx.EVT_BUTTON, self.add_comparision_report, self.frame.buttonOpenComparisionFile)
        self.frame.Bind(wx.EVT_BUTTON, self.add_supplier_files, self.frame.buttonOpenSupplierPrices)

        self.frame.Bind(wx.EVT_BUTTON, self.del_ulc_row, self.frame.buttonDeleteRow)
        self.frame.Bind(wx.EVT_BUTTON, self.clearULC, self.frame.buttonClearAllUlc)


    def add_cheescake_preport(self, event):
        self.view_data.cheescake_report = self.open_file_dialog()
        self.frame.input_CheesCake.LabelText = self.view_data.cheescake_report.GetFilename()


    def add_comparision_report(self, event):
        self.view_data.comparision_file = self.open_file_dialog()
        self.frame.input_comparision.LabelText = self.view_data.comparision_file.GetFilename()

    def add_supplier_files(self, event):
        self.view_data.supplierFiles = self.open_files_dialog()
        self.add_ulc_items()

    def add_ulc_items(self):
        file_names = self.view_data.supplierFiles.GetFilenames()
        for i in range(0, len(file_names)):
            self.frame.ulc.InsertStringItem(i, file_names[i])
            self.frame.ulc.SetItemWindow(i, 1, self.create_combobox_ulc())
        self.frame.ulc.Refresh()

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

    def start_parse_1(self):
        my_parser = parser.Parser()
        uchList = my_parser.get_products_list(self.view_data.cheescake_report.GetPath())
        complist = my_parser.get_products_list(self.view_data.comparision_file.GetPath())
        for file_path in self.view_data.supplierFiles.GetPaths():
            pass




    def start_parse(self, view_Data: viewData):
        supplierLists = []
        my_parser = parser.Parser()
        uchList = my_parser.get_products_list(view_Data.cheescake_report)
        complist = my_parser.get_products_list(view_Data.comparision_file)
        for item in view_Data.supplierFiles:
            supplierLists.append(my_parser.get_products_list(item))
        rs = resultCreater.ResultCreater(supplierLists, uchList, complist).createResultList()
        self.export_to_excel(rs)


    def export_to_excel(self, my_data):
        fileReader.FileReader().to_excel(my_data)
