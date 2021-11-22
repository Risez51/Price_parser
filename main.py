import comparisionParser
import supplierParser
import unloadedCheescakeParser


def main():
    darsiFile = supplierParser.SupplierParser("_Прайс 21 Дарси.xlsx",2,4)
    darsiFile.sheet =1
    darsiProducts = darsiFile.getProductListFromXlsx()

    mirInstrumentaFile = supplierParser.SupplierParser("Прайс Мир инструмента.xls",0,8)
    mirInstrumentaProducts = mirInstrumentaFile.getProductListFromXlsx()

    compFile = comparisionParser.ComparisionParser("КГК таблица соответствий.xlsx")
    complist = compFile.getComparisionList()
    supplierLists = []
    supplierLists.append({"Дарси": darsiProducts})
    supplierLists.append({"Мир инструментов": mirInstrumentaProducts})

    uchFile = unloadedCheescakeParser.UnloadedCheescakeParser("выгрузка_чизкейк.xlsx")
    uchList = uchFile.getUnloadedCheescakeList()

    print(f'в файле Прайс Мир инструмента.xls найдено {len(mirInstrumentaProducts)} товаров')
    print(f'в файле _Прайс 21 Дарси.xlsx найдено {len(darsiProducts)} товаров')
    print(f'в файле КГК таблица соответствий.xlsx найдено {len(complist)} товаров')
    print(f'в файле выгрузка_чизкейк.xlsx найдено {len(uchList)} товаров')
if __name__ == "__main__":
        main()

