from view import mainForm
import wx
from view import myWindow
from controller import controllers


def main():
    app = wx.App()
    controllers.Controllers(app)
    app.MainLoop()


if __name__ == "__main__":
    main()
