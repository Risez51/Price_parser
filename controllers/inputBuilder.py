class InputBuilder:
    def __init__(self, view_items):
        self.view_items = view_items

    def update_input_cheescake_label(self, my_input, file_dict):
        if file_dict is not None:
            for file_name in file_dict:
                my_input.LabelText = file_name
                self.view_items.update_cheescake_report(file_dict.get(file_name))

    def update_input_comparison_label(self, my_input, file_dict):
        if file_dict is not None:
            for file_name in file_dict:
                my_input.LabelText = file_name
                self.view_items.update_comparison_report(file_dict.get(file_name))

    def update_input_liquidity_label(self, my_input, file_dict):
        if file_dict is not None:
            for file_name in file_dict:
                my_input.LabelText = file_name
                self.view_items.update_liquidity_report(file_dict.get(file_name))

    def update_input_items(self):
        self.view_items.file_tag_path_dict.update(self.view_items.file_tag_path_cheescake_report)
        self.view_items.file_tag_path_dict.update(self.view_items.file_tag_path_comparison_report)
        #self.view_items.file_tag_path_dict.update(self.view_items.file_tag_path_liquidity_report)
