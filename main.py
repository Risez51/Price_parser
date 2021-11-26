from model import resultCreater, supplierParser, unloadedCheescakeParser, comparisionParser
from view import mainForm
import wx
def main():
    #runModel()

    # Здесь происходит создание экземпляра нашей программы, которая впоследствии и будет запущена.
    app = wx.App()
    mainWindow = mainForm.MainForm(None, "Прайс-парсер")
    mainWindow.Center()
    mainWindow.Show()
    app.MainLoop()


def runModel():
    darsiFile = supplierParser.SupplierParser("C:\\Users\\OperTech\\pythonProject\\pythonProject\\Price_parser\\_Прайс 21 Дарси.xlsx", 2, 4, 0)
    darsiProducts = darsiFile.getProductListFromXlsx()

    mirInstrumentaFile = supplierParser.SupplierParser("C:\\Users\\OperTech\\pythonProject\\pythonProject\\Price_parser\\Прайс Мир инструмента.xls", 0, 8, 0)
    mirInstrumentaProducts = mirInstrumentaFile.getProductListFromXlsx()

    compFile = comparisionParser.ComparisionParser("C:\\Users\\OperTech\\pythonProject\\pythonProject\\Price_parser\\КГК таблица соответствий.xlsx")
    complist = compFile.getComparisionList()
    supplierLists = []
    supplierLists.append({"Дарси 1": darsiProducts})
    supplierLists.append({"Мир инструментов 1": mirInstrumentaProducts})

    uchFile = unloadedCheescakeParser.UnloadedCheescakeParser("C:\\Users\\OperTech\\pythonProject\\pythonProject\\Price_parser\\china2.xlsx")
    uchList = uchFile.getUnloadedCheescakeList()

    rs = resultCreater.ResultCreater(supplierLists, uchList, complist)
    rList = rs.createResultList()
    rs.getResultExcelFile(rList)

    print(f'в rList найдено {len(rList)} товаров')
    print(f'в файле Прайс Мир инструмента.xls найдено {len(mirInstrumentaProducts)} товаров')
    print(f'в файле _Прайс 21 Дарси.xlsx найдено {len(darsiProducts)} товаров')
    print(f'в файле КГК таблица соответствий.xlsx найдено {len(complist)} товаров')
    print(f'в файле выгрузка_чизкейк.xlsx найдено {len(uchList)} товаров')


if __name__ == "__main__":
        main()