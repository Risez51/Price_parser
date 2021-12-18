import re


class Bookkeeper:
    def get_procent_difference(self, supplier_price, holding_price):
        if holding_price == '0' or holding_price == '0.00' or supplier_price == "0.00" or supplier_price == "":
            return ''
        p_hold = self.get_float_from_price(self.get_price_without_nds(holding_price))
        p_sup = self.get_float_from_price(supplier_price)
        one_procent = p_hold / 100
        procent = (p_sup / one_procent) - 100
        return f'{procent:.2f}%'

    def get_price_expenses(self, holding_purchase_price, holding_supplier_brand):
        if holding_supplier_brand == "SHAN DONG DONGPING JIUXIN HARDWARE TOOLS CO.,LTD" or \
                holding_supplier_brand == "QINGDAO LEAD WORLD IMP&EXP CO., LTD":

            return self.get_float_from_price(holding_purchase_price) * 1.2
        elif holding_supplier_brand == "SHANGHAI UNI-STAR INDUSTRIAL & TRADING CO., LTD":
            return self.get_float_from_price(holding_purchase_price) * 1.1
        else:
            return self.get_float_from_price(holding_purchase_price)

    def get_price_without_nds(self, price):
        return f'{self.get_float_from_price(price) / 1.2:.2f}'

    def get_float_from_price(self, price):
        price = self.reg_price(price)
        return float(price) if float(price) else 0

    @staticmethod
    def reg_price(price):
        return re.search(r'\d{1,}(\.|\,)?\d{0,2}', price).group(0)
