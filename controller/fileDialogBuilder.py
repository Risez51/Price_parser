import wx


class FileDialog:
    def __init__(self, frame):
        self.frame = frame

    # Возвращает словарь {'имя файла': 'путь к файлу'}
    def open_file(self):
        return self.open_files_dialog(self.frame, wx.FD_OPEN)

    # Возвращает словарь {'имя файла': 'путь к файлу', ...,n}
    def open_files(self):
        return self.open_files_dialog(self.frame, wx.FD_MULTIPLE)

    def open_files_dialog(self, frame, param):
        file_dialog = wx.FileDialog(
            frame,
            message="Добавить файлы...",
            defaultDir=".",
            defaultFile="",
            wildcard="*.xls; *.xlsx; *.csv",
            style=param)
        if file_dialog.ShowModal() == wx.ID_OK:
            if param == wx.FD_MULTIPLE:
                return self.get_dicts_by_dlg(file_dialog)
            elif param == wx.FD_OPEN:
                return self.get_dict_by_dlg(file_dialog)
        elif file_dialog.ShowModal() == wx.ID_EXIT:
            pass
        file_dialog.Destroy()

    # На входе файл диалог на выходы словрь {'имя файла': 'путь к файлу'}
    def get_dict_by_dlg(self, file_dialog):
        return {file_dialog.GetFilename(): file_dialog.GetPath()}

    # На входе файл диалог на выходы словрь {'имя файла': 'путь к файлу', ...,n}
    def get_dicts_by_dlg(self, file_dialog):
        result = {}
        for file_path in file_dialog.GetPaths():
            result.update({self.get_filename(file_path): file_path})
        return result

    @staticmethod
    def get_filename(file_path):
        return file_path.split('\\')[-1]
