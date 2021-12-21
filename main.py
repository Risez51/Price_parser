import wx
from controllers import controller


def main():
    app = wx.App()
    controller.Controller(app)
    app.MainLoop()


if __name__ == "__main__":
    main()
