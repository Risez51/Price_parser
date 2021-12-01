from model import resultCreater, supplierParser, unloadedCheescakeParser, comparisionParser
class Controllers:
    def __init__(self):
        pass

    def parse(self, view_Data):
        supplierLists = []

        uchFile = unloadedCheescakeParser.UnloadedCheescakeParser(view_Data.cheescake_report)
        uchList = uchFile.getUnloadedCheescakeList()

        compFile = comparisionParser.ComparisionParser(view_Data.comparision_file)
        complist = compFile.getComparisionList()

        for price_file in view_Data.supplierFiles:

            #print(f'{list(items)[0]} - ЭТО ЛИСТ АЙТЕМС[0]')
            if list(price_file.keys())[0] == "Дарси 1":
                #print(f'{list(price_file.keys())[0]} - ЭТО ЛИСТ АЙТЕМС[0] ДАРСИ' )
                #print(f'{str(price_file.get(list(price_file.keys())[0]))} - ЭТО ЛИСТ АЙТЕМС[1] ДАРСИ')
                darsiFile = supplierParser.SupplierParser(
                    str(price_file.get(list(price_file.keys())[0])), 2, 4, 0)
                darsiProducts = darsiFile.getProductListFromXlsx()
                supplierLists.append({"Дарси 1": darsiProducts})
            elif list(price_file.keys())[0] == "Мир инструментов 1":
                #print(f'{list(price_file.keys())[0]} - ЭТО ЛИСТ АЙТЕМС[0] МИР ИНСТРУЕНТОВ 1')
                mirInstrumentov = supplierParser.SupplierParser(
                    str(price_file.get(list(price_file.keys())[0])), 0, 8, 0)
                mirInstrumentovProducts = mirInstrumentov.getProductListFromXlsx()
                supplierLists.append({"Мир инструментов 1": mirInstrumentovProducts})
            else:
                pass

        rs = resultCreater.ResultCreater(supplierLists, uchList, complist)
        rList = rs.createResultList()
        rs.getResultExcelFile(rList)
