class RadioBuilder:
    def __init__(self, radiogroup, view_items):
        self.view_items = view_items
        self.radiogroup = radiogroup

    def update_radiogroup_value(self):
        self.view_items.radiogroup_value = self.radiogroup.GetString(self.radiogroup.GetSelection())