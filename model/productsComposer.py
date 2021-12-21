from model import unloadedCheescakeItem, bookkeeper, config, composedItem


class ProductsComposer:
    def __init__(self, products_dict):
        self.bookkeeper = bookkeeper.Bookkeeper()
        self.cnfg = config.Config()
        self.products_dict = products_dict
        self.uchList = self.products_dict.pop(self.cnfg.cheescake_report_name())
        self.comparisionList = self.products_dict.pop(self.cnfg.comparison_report_name())

    def create_result_for_one_sheet(self):
        result_items_list = []
        for comparision_item in self.comparisionList:
            composed_item = composedItem.ComposedItem()
            for supplier_name in self.products_dict:
                composed_item.create_composed_item(supplier_name,
                                                   self.get_uchItem(comparision_item.holding_article),
                                                   comparision_item,
                                                   self.products_dict.get(supplier_name))
                #добавлять в лист только если компосед итем не пустой словарь
                if composed_item.item_data:
                    result_items_list.append(composed_item.item_data)
        return result_items_list

    def create_result_for_several_sheets(self):
        group_names_list = list(set([comparison_item.holding_group for comparison_item in self.comparisionList]))
        #словарь {Имя_листа_эксель: продукты для этого листа}
        result_dict = {}
        for group_name in group_names_list:
            result_dict.update({group_name: []})
        for comparison_item in self.comparisionList:
            composed_item = composedItem.ComposedItem()
            for supplier_name in self.products_dict:
                composed_item.create_composed_item(supplier_name,
                                                   self.get_uchItem(comparison_item.holding_article),
                                                   comparison_item,
                                                   self.products_dict.get(supplier_name))
                if composed_item.item_data:
                    result_dict.get(comparison_item.holding_group).append(composed_item.item_data)
        return result_dict

    def get_uchItem(self, article):
        for uch_item in self.uchList:
            if article == uch_item.article:
                return uch_item
        return unloadedCheescakeItem.UnloadedCheescakeItem()



