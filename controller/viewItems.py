import re
from model import config

class ViewItems:
    def __init__(self):
        self.file_name_path_dict = {}
        self.file_tag_path_dict = {}

    def update_cheescake_report(self, file_path):
        print({config.Config().cheescake_report_name(): file_path})
        self.file_tag_path_dict.update({config.Config().cheescake_report_name(): file_path})

    def update_comparison_report(self, file_path):
        self.file_tag_path_dict.update({config.Config().comparison_report_name(): file_path})


    @staticmethod
    def get_filename(file_path):
        return re.match(r'[\w-]+\..*$', file_path).group(0)



