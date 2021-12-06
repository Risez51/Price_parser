from model import resultCreater, supplierParser, unloadedCheescakeParser, comparisionParser, fileReader, viewData, \
    parser


class Controllers:
    def __init__(self):
        pass

    def parse(self, view_Data: viewData):
        supplierLists = []

        my_parser = parser.Parser()
        uchList = my_parser.get_products_list(view_Data.cheescake_report)
        complist = my_parser.get_products_list(view_Data.comparision_file)

        for item in view_Data.supplierFiles:
            supplierLists.append(my_parser.get_products_list(item))

        rs = resultCreater.ResultCreater(supplierLists, uchList, complist).createResultList()
        self.export_to_excel(rs)

    def export_to_excel(self, my_data):
        fileReader.FileReader().to_excel(my_data)
