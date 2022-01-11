import re
from model import config

class ViewItems:
    def __init__(self):
        self.file_name_path_dict = {}
        self.file_tag_path_dict = {}
        self.file_tag_path_cheescake_report = {}
        self.file_tag_path_comparison_report = {}
        self.file_tag_path_liquidity_report = ''
        self.radiogroup_value = ''

    def update_cheescake_report(self, file_path):
        self.file_tag_path_cheescake_report.update({config.Config().get_cheescake_report_name(): file_path})

    def update_comparison_report(self, file_path):
        self.file_tag_path_comparison_report.update({config.Config().get_comparison_report_name(): file_path})

    def update_liquidity_report(self, file_path):
        self.file_tag_path_liquidity_report = file_path

    def update_radiogroup_value(self, radiogroup):
        return radiogroup.GetString(radiogroup.GetSelection())

    @staticmethod
    def get_filename(file_path):
        return re.match(r'[\w-]+\..*$', file_path).group(0)



