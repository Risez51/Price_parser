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

        # Первая строка (добавление файла: отчет/выгрузка(china2) из Cheesсake)
        v_box1 = wx.BoxSizer(wx.HORIZONTAL)
        label_cheescake = wx.StaticText(self.mainPanel, label="Отчет чизкейк:")
        self.input_cheescake = wx.TextCtrl(self.mainPanel, style=wx.TE_READONLY)
        self.button_cheescake = wx.Button(self.mainPanel, wx.ID_ANY, "Добавить")
        v_box1.Add(label_cheescake, flag=wx.RIGHT, border=8)
        v_box1.Add(self.input_cheescake, proportion=1)
        v_box1.Add(self.button_cheescake, flag=wx.RIGHT | wx.LEFT, border=8)

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

        # Третья строка (добавление таблицы ликвидности)
        h_box30 = wx.BoxSizer(wx.HORIZONTAL)
        label_liquidity = wx.StaticText(self.mainPanel, label="Таблица            \nликвидности:")
        self.input_liquidity = wx.TextCtrl(self.mainPanel, style=wx.TE_READONLY)
        self.buttonOpenLiquidityFile = wx.Button(self.mainPanel, wx.ID_ANY, "Добавить")
        h_box30.Add(label_liquidity, flag=wx.RIGHT, border=8)
        h_box30.Add(self.input_liquidity, proportion=1)
        h_box30.Add(self.buttonOpenLiquidityFile, flag=wx.RIGHT | wx.LEFT, border=8)

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

        # RadioGroup
        v_box65 = wx.BoxSizer(wx.VERTICAL)
        self.rbox = wx.RadioBox(self.mainPanel, label='Скомпоновать:', pos=(80, 10),
                                choices=['В 1 файл', 'По группам'],
                                majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        v_box65.Add(self.rbox, flag=wx.ALIGN_RIGHT|wx.TOP| wx.RIGHT, border=5)

        # Кнопка управление приложением Спарсить/Очистить
        h_box7 = wx.BoxSizer(wx.HORIZONTAL)
        v_box71 = wx.BoxSizer(wx.VERTICAL)
        v_box72 = wx.BoxSizer(wx.VERTICAL)
        v_box73 = wx.BoxSizer(wx.VERTICAL)

        self.buttonClearAllUlc = wx.Button(self.mainPanel, wx.ID_ANY, label="Очистить все", size=(90, 30))
        self.buttonDeleteRow = wx.Button(self.mainPanel, wx.ID_ANY, label="Удалить файл", size=(90, 30))
        self.buttonParse = wx.Button(self.mainPanel, wx.ID_ANY, label="Спарсить", size=(90, 30))
        self.buttonTest = wx.Button(self.mainPanel, wx.ID_ANY, label="Test", size=(90, 30))

        v_box71.Add(self.buttonDeleteRow, flag=wx.ALIGN_LEFT | wx.LEFT | wx.RIGHT, border=10)
        v_box71.Add(self.buttonTest, flag=wx.ALIGN_LEFT | wx.LEFT | wx.RIGHT, border=10)
        v_box72.Add(self.buttonClearAllUlc, flag=wx.ALIGN_LEFT | wx.RIGHT, border=250)
        v_box73.Add(self.buttonParse, proportion=1, flag=wx.ALIGN_RIGHT | wx.LEFT | wx.RIGHT, border=10)
        h_box7.Add(v_box71, flag=wx.EXPAND)
        h_box7.Add(v_box72, flag=wx.EXPAND)
        h_box7.Add(v_box73, flag=wx.EXPAND)


        # Добавление элементов в главный сайзер приложения VBOX
        self.vbox.Add(v_box1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(h_box2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(h_box30, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(h_box3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(h_box4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.vbox.Add(h_box5, proportion=1, flag=wx.EXPAND | wx.BOTTOM | wx.TOP, border=10)
        self.vbox.Add(h_box6, flag=wx.EXPAND)
        self.vbox.Add(v_box65, flag=wx.EXPAND, border=10)
        self.vbox.Add(h_box7, flag=wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.TOP, border=10)
        #self.vbox.Add(h_box7, flag=wx.EXPAND | wx.BOTTOM | wx.RIGHT | wx.TOP, border=10)

        # Добавление VBOX на главную панель рабочей области
        self.mainPanel.SetSizer(self.vbox)
