from model import config
class ViewData:
    def __init__(self):
        self.supplierFiles = []
        self.all_supplier_list = config.Config().supplier_names