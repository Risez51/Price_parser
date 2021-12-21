import pandas as pd
import datetime
import openpyxl


class FileReader:
    def __init__(self, sheet=0):
        self.sheet = sheet

    def get_list_from_excel(self, file_path: str):
        return pd.ExcelFile(file_path).parse(sheet_name=self.sheet).to_numpy()

    def get_list_from_csv(self, file_path: str):
        return pd.read_csv(file_path, sep=";", engine='python', encoding='latin-1').to_numpy()


    def get_data_list(self, file_path):
        return self.get_list_from_excel(file_path) if ".xl" in file_path else self.get_list_from_csv(file_path)


class FileWriter:
    def __init__(self, sheet=0):
        self.sheet = sheet

    def to_excel_on_one_sheet(self, my_data):
        my_date = datetime.datetime.now()
        file_name = f'./Отчет (от {my_date.day}-{my_date.month}-{my_date.year}) (в {my_date.hour}-{my_date.minute}).xlsx'
        pd.DataFrame(data=my_data).to_excel(file_name, index=False)

    def to_excel_on_several_sheets(self, my_data):
        my_date = datetime.datetime.now()
        file_name = f'./Отчет (от {my_date.day}-{my_date.month}-{my_date.year}) (в {my_date.hour}-{my_date.minute}).xlsx'
        pd.DataFrame(data=[]).to_excel(file_name)
        with pd.ExcelWriter(file_name, mode='a', engine='openpyxl') as writer:
            for sheet_name in my_data:
                if my_data.get(sheet_name):
                    pd.DataFrame(data=my_data.get(sheet_name)).to_excel(writer, sheet_name=sheet_name, index=False)
            writer.book.remove(writer.book['Sheet1'])
