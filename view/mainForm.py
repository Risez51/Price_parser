import wx
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
        input_CheesCake = wx.TextCtrl(self.mainPanel, style=wx.TE_READONLY)
        buttonOpenCheesCakeFile = wx.Button(self.mainPanel, wx.ID_ANY, "Добавить")
        hbox1.Add(label_CheesCake, flag=wx.RIGHT, border=8)
        hbox1.Add(input_CheesCake, proportion=1)
        hbox1.Add(buttonOpenCheesCakeFile, flag=wx.RIGHT | wx.LEFT, border=8)


        #линия сепаратор 15
        hbox15 = wx.BoxSizer(wx.HORIZONTAL)
        sep15 = wx.StaticLine(self.mainPanel)
        hbox15.Add(sep15, flag=wx.EXPAND, proportion=1)


        #Вторая строка (добавление файла соответствий)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        label_comparision = wx.StaticText(self.mainPanel, label="Таблица \nсоответствий:")
        input_comparision = wx.TextCtrl(self.mainPanel, style=wx.TE_READONLY)
        buttonOpenComparisionFile = wx.Button(self.mainPanel, wx.ID_ANY, "Добавить")
        hbox2.Add(label_comparision, flag=wx.RIGHT, border=8)
        hbox2.Add(input_comparision, proportion=1)
        hbox2.Add(buttonOpenComparisionFile, flag=wx.RIGHT | wx.LEFT, border=8)


        # Добавление прайсов на лист
        hbox25 = wx.BoxSizer(wx.HORIZONTAL)
        buttonOpenSupplierPrices = wx.Button(self.mainPanel, wx.ID_ANY, label="Добавить прайсы поставщиков", size=(0,40))
        buttonOpenSupplierPrices.Bind(wx.EVT_BUTTON, self.openSupplierFiles)
        hbox25.Add(buttonOpenSupplierPrices, flag=wx.EXPAND, proportion=1)


        #Рабочая область - таблица добавленных файлов поставщика:
        self.hbox3 = wx.BoxSizer(wx.VERTICAL)
        self.workPanel = wx.Panel(self.mainPanel,size=(600,300))
        self.workPanel.SetBackgroundColour(wx.GREEN)
        self.hbox3.Add(self.workPanel)

        self.l = ["Дарси", "Мир инструмента"]
        #Кнопка управление приложением Спарсить/Очистить
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        buttonParse = wx.Button(self.mainPanel, wx.ID_ANY, label="Спарсить", size=(70,30))
        buttonDeleteFile = wx.Button(self.mainPanel, wx.ID_ANY, label="Очистить", size=(70,30))
        hbox4.Add(buttonParse, flag=wx.LEFT, border=10)
        hbox4.Add(buttonDeleteFile, flag=wx.LEFT, border=10)


        #добавление элементов в главный сайзер приложения VBOX
        self.vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(hbox15, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=5)
        self.vbox.Add(hbox25, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=5)
        self.vbox.Add(self.hbox3, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(hbox4, flag=wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT | wx.TOP, border=10)


        #Добавление VBOX на главную панель рабочей области
        self.mainPanel.SetSizer(self.vbox)




    def openSupplierFiles(self, event):
        dlg = wx.FileDialog(
            self, message="Добавить файлы...",
            defaultDir=".",
            defaultFile="", wildcard="*.*", style=wx.FD_MULTIPLE)
        if dlg.ShowModal() == wx.ID_OK:
            pathList = dlg.GetPaths()
            myGrid = wx.GridSizer(len(pathList), 2, 0 ,0)
            for item in pathList:
                myGrid.Add((wx.TextCtrl(self.workPanel,wx.ID_ANY, item)), flag=wx.EXPAND, proportion=1)
                myGrid.Add((wx.Choice(self.workPanel)), flag=wx.EXPAND, proportion=1)
            self.workPanel.SetSizer(myGrid)
        dlg.Destroy()


    def onAbout(self, event):
        dlg = wx.MessageDialog(self, "Message in MessageDialog","Title", wx.OK)
        dlg.ShowModal()


    def onExit(self, event):
        wx.Exit()
        pass


