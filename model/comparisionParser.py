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
            #Дарси
            compItem.darsi_article_sibin = self.fix_str(item[18])
            compItem.darsi_brand_sibin = item[19]
            compItem.darsi_article_stayer = self.fix_str(item[20])
            compItem.darsi_brand_stayer = item[21]
            compItem.darsi_article_zubr = self.fix_str(item[22])
            compItem.darsi_brand_zubr = item[23]
            compItem.darsi_article_mirax = self.fix_str(item[24])
            compItem.darsi_brand_mirax = item[25]
            compItem.darsi_article_kraftool = self.fix_str(item[26])
            compItem.darsi_brand_kraftool = item[27]
            #Ипц
            compItem.inpo_article_cnic = str(item[28]).replace(".0", "")
            compItem.inpo_brand_cnic = item[29]
            compItem.inpo_article_tlx = str(item[30]).replace(".0", "")
            compItem.inpo_brand_tlx = item[31]
            #Мир инструментов
            compItem.mirInstrumentov_article_sibrteh = self.fix_str(item[32])
            compItem.mirInstrumentov_brand_sibrteh = item[33]
            compItem.mirInstrumentov_article_cinc_sibrteh = self.fix_str(item[34])
            compItem.mirInstrumentov_brand_cinc_sibrteh = item[35]
            compItem.mirInstrumentov_article_matrix = self.fix_str(item[36])
            compItem.mirInstrumentov_brand_matrix = item[37]
            compItem.mirInstrumentov_article_sparta = self.fix_str(item[38])
            compItem.mirInstrumentov_brand_sparta = item[39]
            compItem.mirInstrumentov_article_gross = self.fix_str(item[40])
            compItem.mirInstrumentov_brand_gross = item[41]
            compItem.mirInstrumentov_article_stels = self.fix_str(item[42])
            compItem.mirInstrumentov_brand_stels = item[43]
            #Белый медведь
            compItem.whiteBear_article = self.fix_str(item[44])
            compItem.whiteBear_brand = item[45]
            #Ипц
            compItem.ipk_article = str(item[46]).replace(".0", "")
            compItem.ipk_brand = item[47]
            #Дело техники
            compItem.delo_tehniki_article = str(item[48]).replace(".0", "")
            compItem.delo_tehniki_brand = item[49]
            #ТДСЗ
            compItem.tdsz_article = str(item[50]).replace(".0", "")
            compItem.tdsz_brand = item[51]
            #КЭМ
            compItem.kem_article = self.fix_kem_article(item[52])
            compItem.kem_brand = item[53]
            #Инфорком
            compItem.inforkom_article_forsage = str(item[54]).replace(".0", "")
            compItem.inforkom_brand_forsage = item[55]
            compItem.inforkom_article_partner = str(item[56]).replace(".0", "")
            compItem.inforkom_brand_partner = item[57]
            #Волжский инструмент
            compItem.volzhskij_article = str(item[58]).replace(".0", "")
            compItem.volzhskij_brand = item[59]
            #Ручные инструменты
            compItem.ruchnie_instrumenti_article_resolux = str(item[60]).replace(".0", "")
            compItem.ruchnie_instrumenti_brand_resolux = item[61]
            compItem.ruchnie_instrumenti_article_radiant = str(item[62]).replace(".0", "")
            compItem.ruchnie_instrumenti_brand_radiant = item[63]
            #Кибер инструмент
            compItem.ciber_instrument_article = self.fix_str(item[64])
            compItem.ciber_instrument_brand = item[65]
            #Туламаш
            compItem.tulamash_article = str(item[66]).replace(".0", "")
            compItem.tulamash_brand = item[67]
            #Железный мир
            compItem.zhelezniy_mir_article = str(item[68]).replace(".0", "")
            compItem.zhelezniy_mir_brand = item[69]
            #Дтл
            compItem.dtl_article = self.fix_str(item[70])
            compItem.dtl_brand = item[71]
            #Наш прайс
            compItem.nash_price_article_skinz =str(item[72]).replace(".0", "")
            compItem.nash_price_brand_skinz = item[73]
            compItem.nash_price_article_minz = str(item[74]).replace(".0", "")
            compItem.nash_price_brand_minz = item[75]
            # МеккаИнструмент
            compItem.mekkaInstrument_article = self.fix_str(item[76])
            compItem.mekkaInstrument_brand = item[77]
            # Rinscom
            compItem.rinscom_article = str(item[78]).replace(".0", "")
            compItem.rinscom_brand = item[79]


            comparisionList.append(compItem)
            #Принты для отладки входящих артикулов в файле "Таблица соответствий"
            #print(f'compItem.nash_price_article_skinz: {compItem.nash_price_article_skinz}\n'
            #      f' compItem.nash_price_brand_skinz:{compItem.nash_price_brand_skinz}')
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