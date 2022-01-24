
class ComparisionItem:
    def __init__(self):

        self.holding_name = ""
        self.holding_article = ""
        self.holding_group = ""
        # Автоключ
        self.avtokluch_article_tehmash = ""
        self.avtokluch_brand_tehmash = ""
        self.avtokluch_article_kzsmi = ""
        self.avtokluch_brand_kzsmi = ""
        self.avtokluch_article_niz = ""
        self.avtokluch_brand_niz = ""
        self.avtokluch_article_avtodelo = ""
        self.avtokluch_brand_avtodelo = ""
        self.avtokluch_article_avtom = ""
        self.avtokluch_brand_avtom = ""
        self.avtokluch_article_metallist = ""
        self.avtokluch_brand_metallist = ""
        self.avtokluch_article_tehnik = ""
        self.avtokluch_brand_tehnik = ""
        # Дарси
        self.darsi_article_sibin = ""
        self.darsi_brand_sibin = ""
        self.darsi_article_stayer = ""
        self.darsi_brand_stayer = ""
        self.darsi_article_zubr = ""
        self.darsi_brand_zubr = ""
        self.darsi_article_mirax = ""
        self.darsi_brand_mirax = ""
        self.darsi_article_kraftool = ""
        self.darsi_brand_kraftool = ""
        # Ипц
        self.inpo_article_cnic = ""
        self.inpo_brand_cnic = ""
        self.inpo_article_tlx = ""
        self.inpo_brand_tlx = ""
        # Мир инструментов
        self.mirInstrumentov_article_sibrteh = ""
        self.mirInstrumentov_brand_sibrteh = ""
        self.mirInstrumentov_article_cinc_sibrteh = ""
        self.mirInstrumentov_brand_cinc_sibrteh = ""
        self.mirInstrumentov_article_matrix = ""
        self.mirInstrumentov_brand_matrix = ""
        self.mirInstrumentov_article_sparta = ""
        self.mirInstrumentov_brand_sparta = ""
        self.mirInstrumentov_article_gross = ""
        self.mirInstrumentov_brand_gross = ""
        self.mirInstrumentov_article_stels = ""
        self.mirInstrumentov_brand_stels = ""
        # Белый медведь
        self.whiteBear_article = ""
        self.whiteBear_brand = ""
        # Ипц
        self.ipk_article = ""
        self.ipk_brand = ""
        # Дело техники
        self.delo_tehniki_article = ""
        self.delo_tehniki_brand = ""
        # ТДСЗ
        self.tdsz_article = ""
        self.tdsz_brand = ""
        # КЭМ
        self.kem_article = ""
        self.kem_brand = ""
        # Инфорком
        self.inforkom_article_forsage = ""
        self.inforkom_brand_forsage = ""
        self.inforkom_article_partner = ""
        self.inforkom_brand_partner = ""
        # Волжский инструмент
        self.volzhskij_article = ""
        self.volzhskij_brand = ""
        # Ручные инструменты
        self.ruchnie_instrumenti_article_resolux = ""
        self.ruchnie_instrumenti_brand_resolux = ""
        self.ruchnie_instrumenti_article_radiant = ""
        self.ruchnie_instrumenti_brand_radiant = ""
        # Кибер инструмент
        self.ciber_instrument_article = ""
        self.ciber_instrument_brand = ""
        # Туламаш
        self.tulamash_article = ""
        self.tulamash_brand = ""
        # Железный мир
        self.zhelezniy_mir_article = ""
        self.zhelezniy_mir_brand = ""
        # Дтл
        self.dtl_article = ""
        self.dtl_brand = ""
        # Наш прайс
        self.nash_price_article_skinz = ''
        self.nash_price_brand_skinz = ''
        self.nash_price_article_minz = ''
        self.nash_price_brand_minz = ''
        # МеккаИнструмент
        self.mekkaInstrument_article = ''
        self.mekkaInstrument_brand = ''
        # Rinscom
        self.rinscom_article = ''
        self.rinscom_brand = ''

    def get_values(self, supplier_name):
        if supplier_name == "Дарси":
            return self.get_darsi_params()
        elif supplier_name == "Мир инструмента":
            return self.get_mirInstrumentov_params()
        elif supplier_name == "Белый медведь":
            return self.get_whiteBear_params()
        elif supplier_name == "Ипц":
            return self.get_inpo_params()
        elif supplier_name == "Автоключ":
            return self.get_avtokluch_params()
        elif supplier_name == "Ипк":
            return self.get_ipk_params()
        elif supplier_name == "Дело техники":
            return self.get_delo_teehniki_params()
        elif supplier_name == "ТДСЗ":
            return self.get_tdsz_params()
        elif supplier_name == "КЭМ":
            return self.get_kem_params()
        elif supplier_name == "Инфорком":
            return self.get_inforkom_params()
        elif supplier_name == "Волжский":
            return self.get_volzhskij_params()
        elif supplier_name == "Ручные инструменты":
            return self.get_ruchnie_instrumenti_params()
        elif supplier_name == "Кибер инструмент":
            return self.ciber_instrument_params()
        elif supplier_name == "Туламаш":
            return self.get_tulamash_params()
        elif supplier_name == "Железный мир":
            return self.get_zhelezniy_mir_params()
        elif supplier_name == "Дтл":
            return self.get_dtl_params()
        elif supplier_name == "Наш прайс":
            return self.get_nash_price_params()
        elif supplier_name == 'МеккаИнструмент':
            return self.get_mekkaInstrument_params()
        elif supplier_name == 'Rinscom':
            return self.get_rinscom_params()



    def get_nash_price_params(self):
        return {self.nash_price_article_skinz: self.nash_price_brand_skinz,
                self.nash_price_article_minz: self.nash_price_brand_minz}

    def get_rinscom_params(self):
        return {self.rinscom_article: self.rinscom_brand}

    def get_mekkaInstrument_params(self):
        return {self.mekkaInstrument_article: self.mekkaInstrument_brand}

    def get_dtl_params(self):
        return {self.dtl_article: self.dtl_brand}

    def get_zhelezniy_mir_params(self):
        return {self.zhelezniy_mir_article: self.zhelezniy_mir_brand}

    def get_tulamash_params(self):
        return {self.tulamash_article: self.tulamash_brand}

    def ciber_instrument_params(self):
        return {self.ciber_instrument_article: self.ciber_instrument_brand}

    def get_ruchnie_instrumenti_params(self):
        return {self.ruchnie_instrumenti_article_resolux: self.ruchnie_instrumenti_brand_resolux,
                self.ruchnie_instrumenti_article_radiant: self.ruchnie_instrumenti_brand_radiant}

    def get_volzhskij_params(self):
        return {self.volzhskij_article: self.volzhskij_brand}

    def get_inforkom_params(self):
        return {self.inforkom_article_forsage: self.inforkom_brand_forsage,
                self.inforkom_article_partner: self.inforkom_brand_partner}

    def get_kem_params(self):
        return {self.kem_article: self.kem_brand}

    def get_tdsz_params(self):
        return {self.tdsz_article: self.tdsz_brand}

    def get_delo_teehniki_params(self):
        return {self.delo_tehniki_article: self.delo_tehniki_brand}

    def get_avtokluch_params(self):
        return {self.avtokluch_article_tehmash: self.avtokluch_brand_tehmash,
                self.avtokluch_article_kzsmi: self.avtokluch_brand_kzsmi,
                self.avtokluch_article_niz: self.avtokluch_brand_niz,
                self.avtokluch_article_avtodelo: self.avtokluch_brand_avtodelo,
                self.avtokluch_article_avtom: self.avtokluch_brand_avtom,
                self.avtokluch_article_metallist: self.avtokluch_brand_metallist,
                self.avtokluch_article_tehnik: self.avtokluch_brand_tehnik}

    def get_ipk_params(self):
        return {self.ipk_article: self.ipk_brand}

    def get_darsi_params(self):
        return {self.darsi_article_sibin: self.darsi_brand_sibin,
                self.darsi_article_stayer: self.darsi_brand_stayer,
                self.darsi_article_zubr: self.darsi_brand_zubr,
                self.darsi_article_mirax: self.darsi_brand_mirax,
                self.darsi_article_kraftool: self.darsi_brand_kraftool}

    def get_inpo_params(self):
        return {self.inpo_article_cnic: self.inpo_brand_cnic,
                self.inpo_article_tlx: self.inpo_brand_tlx}

    def get_whiteBear_params(self):
        return {self.whiteBear_article: self.whiteBear_brand}

    def get_mirInstrumentov_params(self):
        return {self.mirInstrumentov_article_sibrteh: self.mirInstrumentov_brand_sibrteh,
                self.mirInstrumentov_article_cinc_sibrteh: self.mirInstrumentov_brand_cinc_sibrteh,
                self.mirInstrumentov_article_matrix: self.mirInstrumentov_brand_matrix,
                self.mirInstrumentov_article_sparta: self.mirInstrumentov_brand_sparta,
                self.mirInstrumentov_article_gross: self.mirInstrumentov_brand_gross,
                self.mirInstrumentov_article_stels: self.mirInstrumentov_brand_stels}
