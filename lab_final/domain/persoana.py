class Persoana:
    def __init__(self, idPersoana, nume, adresa, participari):
        self.__idPersoana = idPersoana
        self.__nume = nume
        self.__adresa = adresa
        self.__participari = participari

    def get_idPersoana(self):
        return self.__idPersoana

    def get_nume(self):
        return self.__nume

    def get_adresa(self):
        return self.__adresa

    def get_participari(self):
        return self.__participari

    def set_idPersoana(self, idPersoana):
        self.__idPersoana = idPersoana

    def set_nume(self, nume):
        self.__nume = nume

    def set_adresa(self, adresa):
        self.__adresa = adresa

    def set_participari(self, participari):
        self.__participari = participari

    def __str__(self):
        return f'ID_Persoana: {self.__idPersoana}, Nume: {self.__nume}, Adresa: {self.__adresa}, NrParticipari: {self.__participari} '
