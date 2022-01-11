import pandas
import pandas as pd
import datetime
import openpyxl


class FileReader:
    def __init__(self, sheet=0):
        self.sheet = sheet

    def get_list_from_excel(self, file_path: str):
        return pd.ExcelFile(file_path).parse(sheet_name=self.sheet, encoding_override='CORRECT_ENCODING').to_numpy()

    def get_list_from_csv(self, file_path: str):
        return pd.read_csv(file_path, sep=";", engine='python', encoding='latin-1').to_numpy()

    def get_liquidity_data_frame_from_excel(self, file_path: str):
        if file_path != '':
            df = pd.read_excel(file_path)
            df['артикул'] = df['артикул'].astype(str)
            df.drop(['наименование'], axis=1, inplace=True)
            df.drop(['Цена по прайсу'], axis=1, inplace=True)
            return df
        return pandas.DataFrame()

    def get_data_list(self, file_path):
        return self.get_list_from_excel(file_path) if ".xl" in file_path else self.get_list_from_csv(file_path)


class FileWriter:
    def __init__(self, sheet=0):
        self.sheet = sheet

    def to_excel_on_one_sheet(self, my_data, liquidity_data_frame):
        self.get_merged_df_with_liquidity_df(pd.DataFrame(data=my_data),
                                             liquidity_data_frame).to_excel(self.create_file_name(),
                                                                            index=False)

    def to_excel_on_several_sheets(self, my_data_dicts, liquidity_data_frame):
        file_name = self.create_file_name()
        pd.DataFrame(data=[]).to_excel(file_name)
        with pd.ExcelWriter(file_name,
                            mode='a',
                            engine='openpyxl') as writer:
            for sheet_name in my_data_dicts:
                if my_data_dicts.get(sheet_name):
                    self.get_merged_df_with_liquidity_df(pd.DataFrame(data=my_data_dicts.get(sheet_name)),
                                                         liquidity_data_frame).to_excel(writer,
                                                                                        sheet_name=sheet_name,
                                                                                        index=False)
            writer.book.remove(writer.book['Sheet1'])


    def create_file_name(self):
        my_date = datetime.datetime.now()
        return f'./Отчет (от {my_date.day}-{my_date.month}-{my_date.year}) (в {my_date.hour}-{my_date.minute}).xlsx'

    def get_merged_df_with_liquidity_df(self, df_products, df_liquidity):
        if not df_liquidity.empty:
            return pd.merge(df_products,
                            df_liquidity,
                            how='left',
                            left_on='Холдинг, артикул',
                            right_on='артикул')
        else:
            return pd.DataFrame(data=df_products)


