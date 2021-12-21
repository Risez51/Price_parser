import wx


class ViewValidator:
    def __init__(self, frame):
        self.frame = frame

    def is_valid(self):
        if self.is_not_void_input_cheescake():
            self.error_message(
                'Отсутствует отчет чизкейк')
            return False
        elif self.is_not_void_input_comparison():
            self.error_message(
                'Отсутствует таблица соответствий')
            return False
        elif self.is_not_void_uls():
            self.error_message(
                'Отсутствуют прайсы конкурентов')
            return False
        elif self.is_append_file_tag_valid_ulc():
            return False
        return True

    # Если не добавлен файл "Отчет чизкейк"
    def is_not_void_input_cheescake(self):
        return self.frame.input_cheescake.LabelText == ''

    # Если не добавлен файл "Отчет чизкейк"
    def is_not_void_input_comparison(self):
        return self.frame.input_comparision.LabelText == ''

    # Если не добавлен ни один из прайсов поставщика == False
    def is_not_void_uls(self):
        return self.frame.ulc.GetItemCount() == 0

    # Combobox в ULC проверка на пустоту, если один из комбобоксов пуст == False
    def is_append_file_tag_valid_ulc(self):
        # Если не выбран file_tag в комбобоксе формы ULC
        for i in range(self.frame.ulc.GetItemCount()):
            combobox = self.frame.ulc.GetItemWindow(i, 1)
            sup_name = combobox.GetString(combobox.GetSelection())
            if sup_name == '':
                self.error_message(f'Не выбран поставщик для файла: {self.frame.ulc.GetItemText(i)}')
                return True
        return False

    def error_message(self, text):
        dlg = wx.MessageDialog(self.frame, f'{text}', 'Ошибка', wx.OK)
        dlg.ShowModal()
