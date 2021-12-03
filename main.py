from view import mainForm
import wx

def main():
    # Здесь происходит создание экземпляра нашей программы, которая впоследствии и будет запущена.
    app = wx.App()
    mainWindow = mainForm.MainForm(None, "Прайс-парсер")
    mainWindow.Center()
    mainWindow.Show()
    app.MainLoop()


if __name__ == "__main__":
        main()