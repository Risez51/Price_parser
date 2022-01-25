import re


class Bookkeeper:

    def get_average_price(self, composed_item_data: {}):
        count_sup_prices = 0
        total_price = 0.0
        for key_title_name in composed_item_data:
            if self.is_supplier_price_title(key_title_name):

                price = composed_item_data.get(key_title_name)
                #print(f'title_name:{key_title_name}\nprice:{price}')
                if price:
                    count_sup_prices = count_sup_prices + 1
                    total_price = total_price + float(price)

        average_price = total_price / count_sup_prices
        composed_item_data.update({'Средняя цена поставщиков': f'{average_price:.2f}'.replace('.', ','),
                                   'Отклонение от средней цены поставщиков': self.get_procent_difference(average_price, composed_item_data.get('Холдинг, цена продажи'))})

        return composed_item_data

    def get_procent_difference(self, supplier_price, holding_price):
        if holding_price == '0' or holding_price == '0.00' or supplier_price == '0.00' or supplier_price == '':
            return ''
        p_hold = self.get_float_from_price(holding_price)
        p_sup = self.get_float_from_price(supplier_price)
        one_procent = p_hold/100
        procent = (p_sup / one_procent) - 100

        return f'{procent:.2f}%'.replace('.', ',')

    def get_price_expenses(self, holding_purchase_price, holding_supplier_brand):
        if holding_supplier_brand == 'SHAN DONG DONGPING JIUXIN HARDWARE TOOLS CO.,LTD' or \
                holding_supplier_brand == 'QINGDAO LEAD WORLD IMP&EXP CO., LTD':

            return f'{self.get_float_from_price(holding_purchase_price) * 1.2:.2f}'
        elif holding_supplier_brand == 'SHANGHAI UNI-STAR INDUSTRIAL & TRADING CO., LTD':
            return f'{self.get_float_from_price(holding_purchase_price) * 1.1:.2f}'
        else:
            return f'{self.get_float_from_price(holding_purchase_price):.2f}'

    def get_price_without_nds(self, price):
        return f'{self.get_float_from_price(price) / 1.2:.2f}'

    def get_float_from_price(self, price):
        price = self.reg_price(price)
        return float(price) if float(price) else 0

    def is_supplier_price_title(self, title_name):
        price_title = re.search(r'цена$', str(title_name))
        if price_title:
            return True
        else:
            return False

    @staticmethod
    def is_not_void_price(price):
        if price == 0 or price == '' or price == 0.0 or price is None:
            return False
        else:
            return True

    @staticmethod
    def reg_price(price):
        return re.search(r'\d{1,}(\.|\,)?\d{0,2}', str(price)).group(0)


