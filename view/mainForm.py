import wx
from wx.lib.agw import ultimatelistctrl as ULC
from model import viewData
class MainForm(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600, 400))

        self.vd = viewData.ViewData()
        self.pathList = []
        #Верхнее меню
        menu = wx.Menu()
        aboutItem = menu.Append(wx.ID_ABOUT, "Информация", "кнопка about")
        exitItem = menu.Append(wx.ID_EXIT, "Выход\tCTRL+Q", "кнопка exit")
        bar = wx.MenuBar()
        bar.Append(menu, "Файл")
        self.SetMenuBar(bar)


        # бинды верхнего меню
        self.Bind(wx.EVT_MENU, self.onAbout, aboutItem)
        self.Bind(wx.EVT_MENU, self.onExit, exitItem)


        #Рабочая область
        self.mainPanel = wx.Panel(self)
        self.mainPanel.SetBackgroundColour(wx.WHITE)
        self.vbox = wx.BoxSizer(wx.VERTICAL)


        #Первая строка (добавление файла: отчет/выгрузка(china2) из CheesCake)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        label_CheesCake = wx.StaticText(self.mainPanel, label="Отчет чизкейк:")
        self.input_CheesCake = wx.TextCtrl(self.mainPanel, style=wx.TE_READONLY)
        buttonOpenCheesCakeFile = wx.Button(self.mainPanel, wx.ID_ANY, "Добавить")
        hbox1.Add(label_CheesCake, flag=wx.RIGHT, border=8)
        hbox1.Add(self.input_CheesCake, proportion=1)
        hbox1.Add(buttonOpenCheesCakeFile, flag=wx.RIGHT | wx.LEFT, border=8)

        #бинды первой строки Cheescake:
        self.Bind(wx.EVT_BUTTON, self.add_Cheescake_Report, buttonOpenCheesCakeFile)

        #линия сепаратор 15
        hbox15 = wx.BoxSizer(wx.HORIZONTAL)
        sep15 = wx.StaticLine(self.mainPanel)
        hbox15.Add(sep15, flag=wx.EXPAND, proportion=1)


        #Вторая строка (добавление файла соответствий)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        label_comparision = wx.StaticText(self.mainPanel, label="Таблица            \nсоответствий:")
        self.input_comparision = wx.TextCtrl(self.mainPanel, style=wx.TE_READONLY)
        buttonOpenComparisionFile = wx.Button(self.mainPanel, wx.ID_ANY, "Добавить")
        hbox2.Add(label_comparision, flag=wx.RIGHT, border=8)
        hbox2.Add(self.input_comparision, proportion=1)
        hbox2.Add(buttonOpenComparisionFile, flag=wx.RIGHT | wx.LEFT, border=8)

        # бинды второй строки Таблица-соответствий:
        self.Bind(wx.EVT_BUTTON, self.add_Comparision_Report, buttonOpenComparisionFile)

        # Добавление прайсов на лист
        hbox25 = wx.BoxSizer(wx.HORIZONTAL)
        buttonOpenSupplierPrices = wx.Button(self.mainPanel, wx.ID_ANY, label="Добавить прайсы поставщиков", size=(0,
                                                                                                                   40))
        buttonOpenSupplierPrices.Bind(wx.EVT_BUTTON, self.openSupplierFiles)
        hbox25.Add(buttonOpenSupplierPrices, flag=wx.EXPAND, proportion=1)


        #Рабочая область - таблица добавленных файлов поставщика:
        self.l = ["Дарси", "Мир инструмента"]
        self.hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.ulc = ULC.UltimateListCtrl(self.mainPanel, agwStyle=ULC.ULC_HAS_VARIABLE_ROW_HEIGHT | ULC.ULC_REPORT | ULC.ULC_HRULES)
        self.ulc.InsertColumn(0, "Файл", width=350)
        self.ulc.InsertColumn(1, "Поставщик", width=215)
        self.hbox3.Add(self.ulc, proportion=1, flag=wx.EXPAND)


        self.l = ["Дарси", "Мир инструмента"]

        #Кнопка управление приложением Спарсить/Очистить
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)

        buttonParse = wx.Button(self.mainPanel, wx.ID_ANY, label="Спарсить", size=(90, 30))
        buttonParse.SetBackgroundColour(wx.GREEN)
        buttonClearAllUlc = wx.Button(self.mainPanel, wx.ID_ANY, label="Очистить все", size=(90, 30))
        buttonDeleteRow = wx.Button(self.mainPanel, wx.ID_ANY, label="Удалить файл", size=(90, 30))

        #TEST BUTTON
        self.btnTest = wx.Button(self.mainPanel, wx.ID_ANY, label="test", size=(90,30))
        self.Bind(wx.EVT_BUTTON, self.test, self.btnTest)
        hbox4.Add(self.btnTest)

        hbox4.Add(buttonDeleteRow, flag=wx.ALIGN_LEFT)
        hbox4.Add(buttonClearAllUlc, flag=wx.LEFT | wx.RIGHT, border=10)
        hbox4.Add(buttonParse, flag=wx.LEFT | wx.RIGHT, border=10)


        #бинды кнопок управления
        self.Bind(wx.EVT_BUTTON, self.deleteRowInUlc, buttonDeleteRow)
        self.Bind(wx.EVT_BUTTON, self.getDataFromForm, buttonParse)
        self.Bind(wx.EVT_BUTTON, self.clearULC, buttonClearAllUlc)


        #добавление элементов в главный сайзер приложения VBOX
        self.vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(hbox15, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(hbox25, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(self.hbox3, proportion=1, flag=wx.EXPAND | wx.BOTTOM | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(hbox4, flag=wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT | wx.TOP, border=10)


        #Добавление VBOX на главную панель рабочей области
        self.mainPanel.SetSizer(self.vbox)


    def getDataFromForm(self, event):
        self.vd.supplierFiles = []
        rowsCount = self.ulc.GetItemCount()
        for i in range(0, rowsCount):
            a = self.ulc.GetItemText(i)
            b = self.ulc.GetItemWindow(i, 1)
            ind = b.GetSelection()
            if b.GetString(ind) == "":
                self.validatingUltimateList(ind)
                break
            self.vd.supplierFiles.append({f'{b.GetString(ind)}': self.get_path_by_name(a)})
            print(a, b.GetString(ind))
        print(self.vd.supplierFiles)


    def test(self, event):
        for item in self.pathList:
            print(item)

    def get_path_by_name(self, fileName):
        for item in self.pathList:
            if fileName in item:
                return item
        return "не нашел такого файла в списке self.pathList"


    # удаляет все items в UltimateListCtrl
    def clearULC(self, event):
        self.ulc.DeleteAllItems()
        self.pathList = []

    # удаляет 1 выбранный item в UltimateListCtr
    def deleteRowInUlc(self, event):
       if self.ulc.GetFocusedItem() > -1:
            self.del_from_pathList(self.ulc.GetItemText(self.ulc.GetFocusedItem()))
            self.ulc.DeleteItem(self.ulc.GetFocusedItem())

    def del_from_pathList(self, fileName):
        for item in self.pathList:
            if fileName in item:
                self.pathList.remove(item)

    #Добавление файлов в UltimateListCtrl из file_dialog
    def openSupplierFiles(self, event):
        dlg = wx.FileDialog(
            self, message="Добавить файлы...",
            defaultDir=".",
            defaultFile="", wildcard="*.*", style=wx.FD_MULTIPLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.pathList = dlg.GetPaths()
            fileNames = dlg.GetFilenames()
            for i in range(0,len(self.pathList)):
                cm = wx.Choice(self.ulc, id=i)
                cm.AppendItems(self.l)
                self.ulc.InsertStringItem(i,fileNames[i])
                self.ulc.SetItemWindow(i, 1, cm, ULC.ULC_ALIGN_LEFT)
        dlg.Destroy()



    def add_Cheescake_Report(self, event):
        dlg = wx.FileDialog(
            self, message="Добавить файл-отчет выгруженный из Cheescake...",
            defaultDir=".",
            defaultFile="", wildcard="*.*", style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.input_CheesCake.LabelText = dlg.GetFilename()
            self.vd.cheescake_report = dlg.GetPath()
        dlg.Destroy()


    def add_Comparision_Report(self, event):
        dlg = wx.FileDialog(
            self, message="Добавить таблицу соответствий...",
            defaultDir=".",
            defaultFile="", wildcard="*.*", style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.input_comparision.LabelText = dlg.GetFilename()
            self.vd.comparision_file = dlg.GetPath()
        dlg.Destroy()

    #Если choice пустой(не выбран поставщик) - выдает message dialog
    def validatingUltimateList(self, index):
        dlg = wx.MessageDialog(self, "Не выбран поставщик у одного из файлов", "Ошибка", wx.OK)
        dlg.ShowModal()


    def onAbout(self, event):
        dlg = wx.MessageDialog(self, "Message in MessageDialog", "Title", wx.OK)
        dlg.ShowModal()

    # Выход из программы
    def onExit(self, event):
        wx.Exit()
        pass


