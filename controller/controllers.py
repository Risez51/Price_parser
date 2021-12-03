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


        for item in view_Data.supplierFiles:
            for supplierName, supplierFilePath in item.items():
                if supplierName == "Дарси":
                    #SupplierParser(путь к файлу, номер столбца артикул, номер столбца цена, номер столбца бренд | Отсчет с ноля)
                    myFile = supplierParser.SupplierParser(supplierFilePath, 2, 4, 0)
                    productList = myFile.getProductListFromXlsx()
                    supplierLists.append({"Дарси 1": productList})
                    supplierLists.append({"Дарси 2": productList})
                elif supplierName == "Мир инструментов":
                    myFile = supplierParser.SupplierParser(supplierFilePath, 0, 8, 0)
                    productList = myFile.getProductListFromXlsx()
                    supplierLists.append({"Мир инструментов 1": productList})
                    supplierLists.append({"Мир инструментов 2": productList})
                elif supplierName == "Белый медведь":
                    myFile = supplierParser.SupplierParser(supplierFilePath, 1, 3, 0)
                    productList = myFile.getProductListFromXlsx()
                    supplierLists.append({"Белый медведь": productList})
                elif supplierName == "Автоключ":
                    myFile = supplierParser.SupplierParser(supplierFilePath, 0, 7, 0)
                    productList = myFile.getProductListFromXlsx()
                    supplierLists.append({"Автоключ": productList})
                elif supplierName == "Ипц":
                    myFile = supplierParser.SupplierParser(supplierFilePath, 0, 2, 0)
                    productList = myFile.getProductListFromXlsx()
                    supplierLists.append({"Ипц": productList})
                else:
                    pass



        rs = resultCreater.ResultCreater(supplierLists, uchList, complist)
        rList = rs.createResultList()
        rs.getResultExcelFile(rList)
