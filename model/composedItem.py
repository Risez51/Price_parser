from model import bookkeeper


class ComposedItem:
    def __init__(self):
        self.bookkeeper = bookkeeper.Bookkeeper()
        self.item_data = {}

    def create_composed_item(self, supplier_name, uch_item_data, comparison_item_data, supplier_products_list):
        holding_dict = {}
        supplier_dict = {}
        holding_dict.update(self.get_holding_dict_params(uch_item_data, comparison_item_data))
        supplier_dict.update(self.get_supplier_params(supplier_name,
                                                       supplier_products_list,
                                                       comparison_item_data.get_values(supplier_name),
                                                   uch_item_data.selling_price))
        #если словрь поставщика не пустой = добавляем в результирующий словарь
        if supplier_dict:
            self.item_data.update(holding_dict)
            self.item_data.update(supplier_dict)

    def get_supplier_params(self, supplier_name, supplier_products_list, comparison_supplier_articles_brands_dict, holding_price):
        my_dict = {}
        # индекс = количеству столбцов с поставщиком в итоговом файле пример: Дарси 1, ..., Дарси n
        index = 0
        # итерация по словарю {артикул_поставщика: бренд} из таблицы соответствий
        #print(supplier_articles_brands_dict)
        for supplier_article in comparison_supplier_articles_brands_dict:
            if self.is_not_void_product(supplier_article):
                index += 1
                # итерация по листу с продуктами

                for product in supplier_products_list:
                    # если артикул_продукта == артикулу_поставщика
                    if product.article == supplier_article:
                        # добавляем словарь с данными по поставщику: артикул, цену, разницу в цене в %, бренд
                        my_dict.update(self.create_supplier_item_data(supplier_article,
                                                                      product.price,
                                                                      holding_price,
                                                                      comparison_supplier_articles_brands_dict.get(
                                                                          supplier_article),
                                                                      supplier_name,
                                                                      index))
        return my_dict

    def is_not_void_product(self, supplier_article):
        if supplier_article == 'nan' or supplier_article == 0 or supplier_article == '0.0' or supplier_article == '0':
            return False
        else:
            return True

    # создает словрь с данными поставщика
    def create_supplier_item_data(self, supplier_article, supplier_price, holding_price, brand, supplier_name,
                                  index):
        if supplier_article == '':
            return {}
        else:
            my_dict = {f'{supplier_name} {index}, артикул': supplier_article,
                       f'{supplier_name} {index}, цена': self.bookkeeper.get_price_without_nds(supplier_price),
                       f'{supplier_name} {index}, разница цен в %': self.bookkeeper.get_procent_difference(
                           supplier_price, holding_price),
                       f'{supplier_name} {index}, бренд': brand}
            return my_dict

    # создает словрь с данными из таблицы соответствия и отчета чизкейк
    def get_holding_dict_params(self, uch_item, comparision_item):
        result_item = {"Холдинг, артикул": comparision_item.holding_article,
                       "Холдинг, наименование": comparision_item.holding_name,
                       "Холдинг, группа": comparision_item.holding_group,
                       "Холдинг, цена закупки с учетом прочих расходов": self.bookkeeper.get_price_expenses(
                           uch_item.purchase_price,
                           uch_item.supplier_name),
                       "Холдинг, цена продажи": uch_item.selling_price,
                       "Холдинг, остатки": uch_item.stock,
                       "Холдинг, поставщик": uch_item.supplier_name,
                       "Холдинг, дата размещения": uch_item.order_date}
        return result_item
