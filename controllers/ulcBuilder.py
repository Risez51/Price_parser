from wx.lib.agw import ultimatelistctrl as ULC
from model import config
import wx

class ULCBuilder:
    def __init__(self, ulc, view_items):
        self.ulc = ulc
        self.view_items = view_items

    # Добавление строк в UCL виджет из файл диалога
    def add_ulc_items(self, file_dict):
        if file_dict is not None:
            all_supplier_list = config.Config().supplier_names
            self.view_items.file_name_path_dict.update(file_dict)
            for file_name in file_dict:
                self.ulc.InsertStringItem(0, file_name)
                self.ulc.SetItemWindow(0, 1, self.create_combobox_inside_ulc(all_supplier_list), ULC.ULC_ALIGN_LEFT)

        # Создает комбобоксы для ulc компонента
    def create_combobox_inside_ulc(self, all_supplier_list):
        combobox = wx.Choice(self.ulc)
        combobox.AppendItems(all_supplier_list)
        combobox.Bind(wx.EVT_MOUSEWHEEL, self.do_nothing)
        return combobox

    def del_selected_item_from_ulc(self):
        if self.ulc.GetFocusedItem() > -1:
            file_name = self.ulc.GetItemText(self.ulc.GetFocusedItem())
            self.view_items.file_name_path_dict.pop(file_name)
            self.ulc.DeleteItem(self.ulc.GetFocusedItem())

    def read_current_data_from_ulc(self):
        result = {}
        for i in range(self.ulc.GetItemCount()):
            file_name = self.ulc.GetItemText(i)
            sup_name = self.ulc.GetItemWindow(i, 1).GetString(self.ulc.GetItemWindow(i, 1).GetSelection())
            result.update({sup_name: self.view_items.file_name_path_dict.get(file_name)})
        self.view_items.file_tag_path_dict.update(result)

    def clear_ulc_items(self):
        self.ulc.DeleteAllItems()
        self.view_items.file_name_path_dict = {}

    def do_nothing(self, event):
        pass