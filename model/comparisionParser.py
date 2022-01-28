from model import comparisionItem, fileWorker


class ComparisionParser:

    def __init__(self):
        self.file_reader = fileWorker.FileReader()

    def get_products_list(self, path_to_file):
        comparisionList = []
        for item in self.file_reader.get_data_list(path_to_file):
            compItem = comparisionItem.ComparisionItem()
            compItem.holding_name = item[1]
            compItem.holding_article = self.fix_str(item[0])
            compItem.holding_group = item[3]
            #Автоключ
            compItem.avtokluch_article_tehmash = str(item[4]).replace(".0", "")
            compItem.avtokluch_brand_tehmash = item[5]
            compItem.avtokluch_article_kzsmi = str(item[6]).replace(".0", "")
            compItem.avtokluch_brand_kzsmi = item[7]
            compItem.avtokluch_article_niz = str(item[8]).replace(".0", "")
            compItem.avtokluch_brand_niz = item[9]
            compItem.avtokluch_article_avtodelo = str(item[10]).replace(".0", "")
            compItem.avtokluch_brand_avtodelo = item[11]
            compItem.avtokluch_article_avtom = str(item[12]).replace(".0", "")
            compItem.avtokluch_brand_avtom = item[13]
            compItem.avtokluch_article_metallist = str(item[14]).replace(".0", "")
            compItem.avtokluch_brand_metallist = item[15]
            compItem.avtokluch_article_tehnik = str(item[16]).replace(".0", "")
            compItem.avtokluch_brand_tehnik = item[17]
            compItem.avtokluch_article_pavlovo = str(item[18]).replace(".0", "")
            compItem.avtokluch_brand_pavlovo = item[19]
            compItem.avtokluch_article_liinz = str(item[20]).replace(".0", "")
            compItem.avtokluch_brand_liinz = item[21]
            compItem.avtokluch_article_kitay = str(item[22]).replace(".0", "")
            compItem.avtokluch_brand_kitay = item[23]
            #Дарси
            compItem.darsi_article_sibin = self.fix_str(item[24])
            compItem.darsi_brand_sibin = item[25]
            compItem.darsi_article_stayer = self.fix_str(item[26])
            compItem.darsi_brand_stayer = item[27]
            compItem.darsi_article_zubr = self.fix_str(item[28])
            compItem.darsi_brand_zubr = item[29]
            compItem.darsi_article_mirax = self.fix_str(item[30])
            compItem.darsi_brand_mirax = item[31]
            compItem.darsi_article_kraftool = self.fix_str(item[32])
            compItem.darsi_brand_kraftool = item[33]
            #Ипц
            compItem.inpo_article_cnic = str(item[34]).replace(".0", "")
            compItem.inpo_brand_cnic = item[35]
            compItem.inpo_article_tlx = str(item[36]).replace(".0", "")
            compItem.inpo_brand_tlx = item[37]
            #Мир инструментов
            compItem.mirInstrumentov_article_sibrteh = self.fix_str(item[38])
            compItem.mirInstrumentov_brand_sibrteh = item[39]
            compItem.mirInstrumentov_article_cinc_sibrteh = self.fix_str(item[40])
            compItem.mirInstrumentov_brand_cinc_sibrteh = item[41]
            compItem.mirInstrumentov_article_matrix = self.fix_str(item[42])
            compItem.mirInstrumentov_brand_matrix = item[43]
            compItem.mirInstrumentov_article_sparta = self.fix_str(item[44])
            compItem.mirInstrumentov_brand_sparta = item[45]
            compItem.mirInstrumentov_article_gross = self.fix_str(item[46])
            compItem.mirInstrumentov_brand_gross = item[47]
            compItem.mirInstrumentov_article_stels = self.fix_str(item[48])
            compItem.mirInstrumentov_brand_stels = item[49]
            #Белый медведь
            compItem.whiteBear_article = self.fix_str(item[50])
            compItem.whiteBear_brand = item[51]
            #Ипц
            compItem.ipk_article = str(item[52]).replace(".0", "")
            compItem.ipk_brand = item[53]
            #Дело техники
            compItem.delo_tehniki_article = str(item[54]).replace(".0", "")
            compItem.delo_tehniki_brand = item[55]
            #ТДСЗ
            compItem.tdsz_article = str(item[56]).replace(".0", "")
            compItem.tdsz_brand = item[57]
            #КЭМ
            compItem.kem_article = self.fix_kem_article(item[58])
            compItem.kem_brand = item[59]
            #Инфорком
            compItem.inforkom_article_forsage = str(item[60]).replace(".0", "")
            compItem.inforkom_brand_forsage = item[61]
            compItem.inforkom_article_partner = str(item[62]).replace(".0", "")
            compItem.inforkom_brand_partner = item[63]
            compItem.inforkom_article_rockforce = str(item[64]).replace(".0", "")
            compItem.inforkom_brand_rockforce = item[65]
            #Волжский инструмент
            compItem.volzhskij_article = str(item[66]).replace(".0", "")
            compItem.volzhskij_brand = item[67]
            #Ручные инструменты
            compItem.ruchnie_instrumenti_article_resolux = str(item[68]).replace(".0", "")
            compItem.ruchnie_instrumenti_brand_resolux = item[69]
            compItem.ruchnie_instrumenti_article_radiant = str(item[70]).replace(".0", "")
            compItem.ruchnie_instrumenti_brand_radiant = item[71]
            #Кибер инструмент
            compItem.ciber_instrument_article = self.fix_str(item[72])
            compItem.ciber_instrument_brand = item[73]
            #Туламаш
            compItem.tulamash_article = str(item[74]).replace(".0", "")
            compItem.tulamash_brand = item[75]
            #Железный мир
            compItem.zhelezniy_mir_article = str(item[76]).replace(".0", "")
            compItem.zhelezniy_mir_brand = item[77]
            #Дтл
            compItem.dtl_article = str(item[78]).replace(".0", "")
            compItem.dtl_brand = item[79]
            #Наш прайс
            compItem.nash_price_article_skinz = str(item[80]).replace(".0", "")
            compItem.nash_price_brand_skinz = item[81]
            compItem.nash_price_article_minz = str(item[82]).replace(".0", "")
            compItem.nash_price_brand_minz = item[83]
            #МеккаИнструмент
            compItem.mekkaInstrument_article = str(item[84]).replace(".0", "")
            compItem.mekkaInstrument_brand = item[85]
            #Rinscom
            compItem.rinscom_article = str(item[86]).replace(".0", "")
            compItem.rinscom_brand = item[87]



            comparisionList.append(compItem)
            #Принты для отладки входящих артикулов в файле "Таблица соответствий"
            #print(f'мир_инструмента_артикул_сибртех: {compItem.mirInstrumentov_article_sibrteh}\n'
            #      f'мир_инструмента_бренд_сибртех:{compItem.mirInstrumentov_brand_sibrteh}')
        return comparisionList

    #Обрезает пробелы слева и справа
    @staticmethod
    def fix_str(value):
        return str(value).strip()

    #Артикул в прайсе поставщика имеет длину 6 (ноли перед артикулом, например 000001), в таблице соответствий
    #данный артикул хранится со значением 1 - функция дополняет артикул нолями.
    def fix_kem_article(self, article):
        if article != "nan" or article != "0" or article != "":
            article = str(article).replace(".0", "")
            while len(article) < 6:
                article = "0" + article
            return article