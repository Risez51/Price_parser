class InputBuilder:
    def __init__(self, my_input, view_items):
        self.my_input = my_input
        self.view_items = view_items

    def update_input_cheescake_label(self, file_dict):
        if file_dict is not None:
            for file_name in file_dict:
                self.my_input.LabelText = file_name
                self.view_items.update_cheescake_report(file_dict.get(file_name))

    def update_input_comparison_label(self, file_dict):
        if file_dict is not None:
            for file_name in file_dict:
                self.my_input.LabelText = file_name
                self.view_items.update_comparison_report(file_dict.get(file_name))
