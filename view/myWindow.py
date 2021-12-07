import wx
from wx.lib.agw import ultimatelistctrl as ULC


class MyWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600, 500))
        menu = wx.Menu()
        self.aboutItem = menu.Append(wx.ID_ABOUT, "Информация", "кнопка about")
        self.exitItem = menu.Append(wx.ID_EXIT, "Выход\tCTRL+Q", "кнопка exit")
        bar = wx.MenuBar()
        bar.Append(menu, "Файл")
        self.SetMenuBar(bar)

        # Главная панель
        self.mainPanel = wx.Panel(self)
        self.mainPanel.SetBackgroundColour(wx.WHITE)
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        # Первая строка (добавление файла: отчет/выгрузка(china2) из CheesCake)
        v_box1 = wx.BoxSizer(wx.HORIZONTAL)
        label_CheesCake = wx.StaticText(self.mainPanel, label="Отчет чизкейк:")
        self.input_CheesCake = wx.TextCtrl(self.mainPanel, style=wx.TE_READONLY)
        self.buttonOpenCheesCakeFile = wx.Button(self.mainPanel, wx.ID_ANY, "Добавить")
        v_box1.Add(label_CheesCake, flag=wx.RIGHT, border=8)
        v_box1.Add(self.input_CheesCake, proportion=1)
        v_box1.Add(self.buttonOpenCheesCakeFile, flag=wx.RIGHT | wx.LEFT, border=8)

        # линия сепаратор 15
        h_box3 = wx.BoxSizer(wx.HORIZONTAL)
        sep15 = wx.StaticLine(self.mainPanel)
        h_box3.Add(sep15, flag=wx.EXPAND, proportion=1)

        # Вторая строка (добавление файла соответствий)
        h_box2 = wx.BoxSizer(wx.HORIZONTAL)
        label_comparision = wx.StaticText(self.mainPanel, label="Таблица            \nсоответствий:")
        self.input_comparision = wx.TextCtrl(self.mainPanel, style=wx.TE_READONLY)
        self.buttonOpenComparisionFile = wx.Button(self.mainPanel, wx.ID_ANY, "Добавить")
        h_box2.Add(label_comparision, flag=wx.RIGHT, border=8)
        h_box2.Add(self.input_comparision, proportion=1)
        h_box2.Add(self.buttonOpenComparisionFile, flag=wx.RIGHT | wx.LEFT, border=8)

        # Добавление прайсов на лист
        h_box4 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttonOpenSupplierPrices = wx.Button(self.mainPanel, wx.ID_ANY,
                                                  label="Добавить прайсы поставщиков",
                                                  size=(0, 40))

        h_box4.Add(self.buttonOpenSupplierPrices, flag=wx.EXPAND, proportion=1)

        # Рабочая область - таблица добавленных файлов поставщика:
        h_box5 = wx.BoxSizer(wx.HORIZONTAL)
        self.ulc = ULC.UltimateListCtrl(self.mainPanel,
                                        agwStyle=ULC.ULC_HAS_VARIABLE_ROW_HEIGHT | ULC.ULC_REPORT | ULC.ULC_HRULES)
        self.ulc.InsertColumn(0, "Файл", width=350)
        self.ulc.InsertColumn(1, "Поставщик", width=190)
        h_box5.Add(self.ulc, proportion=1, flag=wx.EXPAND)

        # progress bar
        h_box6 = wx.BoxSizer(wx.HORIZONTAL)
        self.progress_bar = wx.Gauge(self.mainPanel, wx.ID_ANY, range=100, size=(580, 20))
        h_box6.Add(self.progress_bar, proportion=1, flag=wx.EXPAND | wx.RIGHT | wx.LEFT, border=3)

        # Кнопка управление приложением Спарсить/Очистить
        h_box7 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttonParse = wx.Button(self.mainPanel, wx.ID_ANY, label="Спарсить", size=(90, 30))
        self.buttonClearAllUlc = wx.Button(self.mainPanel, wx.ID_ANY, label="Очистить все", size=(90, 30))
        self.buttonDeleteRow = wx.Button(self.mainPanel, wx.ID_ANY, label="Удалить файл", size=(90, 30))
        h_box7.Add(self.buttonDeleteRow, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        h_box7.Add(self.buttonClearAllUlc, flag=wx.EXPAND | wx.RIGHT, border=250)
        h_box7.Add(self.buttonParse, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)

        # Добавление элементов в главный сайзер приложения VBOX
        self.vbox.Add(v_box1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(h_box2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(h_box3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(h_box4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(h_box5, proportion=1, flag=wx.EXPAND | wx.BOTTOM | wx.TOP, border=10)
        self.vbox.Add(h_box6, flag=wx.EXPAND)
        self.vbox.Add(h_box7, flag=wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.TOP, border=10)

        # Добавление VBOX на главную панель рабочей области
        self.mainPanel.SetSizer(self.vbox)
