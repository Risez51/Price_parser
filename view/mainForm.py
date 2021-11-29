import wx
from wx.lib.agw import ultimatelistctrl as ULC
class MainForm(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600, 400))


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
        self.ulc = ULC.UltimateListCtrl(self.mainPanel, agwStyle=ULC.ULC_HAS_VARIABLE_ROW_HEIGHT | ULC.ULC_REPORT)
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

        self.vbox.Fit(self.mainPanel)
        #Добавление VBOX на главную панель рабочей области
        self.mainPanel.SetSizer(self.vbox)


    def getDataFromForm(self, event):
        rowsCount = self.ulc.GetItemCount()
        for i in range(0, rowsCount):
            a = self.ulc.GetItemText(i)
            b = self.ulc.GetItemWindow(i, 1)
            ind = b.GetSelection()
            print(a, b.GetString(ind))

    def clearULC(self, event):
        self.ulc.DeleteAllItems()

    def deleteRowInUlc(self, event):
       if self.ulc.GetFocusedItem() > -1:
            self.ulc.DeleteItem(self.ulc.GetFocusedItem())

    def openSupplierFiles(self, event):
        dlg = wx.FileDialog(
            self, message="Добавить файлы...",
            defaultDir=".",
            defaultFile="", wildcard="*.*", style=wx.FD_MULTIPLE)
        if dlg.ShowModal() == wx.ID_OK:
            pathList = dlg.GetPaths()
            fileNames = dlg.GetFilenames()
            for i in range(0,len(pathList)):
                cm = wx.Choice(self.ulc, id=i)
                cm.AppendItems(self.l)
                self.ulc.InsertStringItem(i,pathList[i])
                self.ulc.SetItemWindow(i, 1, cm, ULC.ULC_ALIGN_LEFT)
        dlg.Destroy()


    def add_Cheescake_Report(self, event):
        dlg = wx.FileDialog(
            self, message="Добавить файл-отчет выгруженный из Cheescake...",
            defaultDir=".",
            defaultFile="", wildcard="*.*", style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.input_CheesCake.LabelText = dlg.GetFilename()
        dlg.Destroy()


    def add_Comparision_Report(self, event):
        dlg = wx.FileDialog(
            self, message="Добавить таблицу соответствий...",
            defaultDir=".",
            defaultFile="", wildcard="*.*", style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.input_comparision.LabelText = dlg.GetFilename()
        dlg.Destroy()


    def onAbout(self, event):
        dlg = wx.MessageDialog(self, "Message in MessageDialog", "Title", wx.OK)
        dlg.ShowModal()

    def onExit(self, event):
        wx.Exit()
        pass


