import comparisionParser
import resultCreater
import supplierParser
import unloadedCheescakeParser


def main():
    darsiFile = supplierParser.SupplierParser("_Прайс 21 Дарси.xlsx",2,4)
    darsiFile.sheet =0
    darsiProducts = darsiFile.getProductListFromXlsx()

    mirInstrumentaFile = supplierParser.SupplierParser("Прайс Мир инструмента.xls",0,8)
    mirInstrumentaProducts = mirInstrumentaFile.getProductListFromXlsx()

    compFile = comparisionParser.ComparisionParser("КГК таблица соответствий.xlsx")
    complist = compFile.getComparisionList()
    supplierLists = []
    supplierLists.append({"Дарси 1": darsiProducts})
    supplierLists.append({"Мир инструментов 1": mirInstrumentaProducts})

    uchFile = unloadedCheescakeParser.UnloadedCheescakeParser("china2.xlsx")
    uchList = uchFile.getUnloadedCheescakeList()

    rs = resultCreater.ResultCreater(supplierLists,uchList, complist )
    rList =rs.createResultList()
    rs.getResultExcelFile(rList)




    print(f'в rList найдено {len(rList)} товаров')
    print(f'в файле Прайс Мир инструмента.xls найдено {len(mirInstrumentaProducts)} товаров')
    print(f'в файле _Прайс 21 Дарси.xlsx найдено {len(darsiProducts)} товаров')
    print(f'в файле КГК таблица соответствий.xlsx найдено {len(complist)} товаров')
    print(f'в файле выгрузка_чизкейк.xlsx найдено {len(uchList)} товаров')

if __name__ == "__main__":
        main()

