import pandas as pd
import datetime


class FileReader:
    def __init__(self, sheet=0):
        self.sheet = sheet

    def get_list_from_excel(self, file_path: str):
        return pd.ExcelFile(file_path).parse(sheet_name=self.sheet).to_numpy()

    def get_list_from_csv(self, file_path: str):
        return pd.read_csv(file_path, sep=";", engine='python', encoding='latin-1').to_numpy()

    def to_excel(self, my_data):
        myDate = datetime.datetime.now()

        pd.DataFrame(data=my_data).to_excel(f'./Отчет (от {myDate.day}-{myDate.month}-{myDate.year}) (в {myDate.hour}-{myDate.minute}-{myDate.second}).xlsx',
                                            index=False)

    def get_data_list(self,  file_path: str):
        if ".xl" in file_path:
            return self.get_list_from_excel(file_path)
        elif ".csv" in file_path:
            return self.get_list_from_csv(file_path)
        else:
            return []




