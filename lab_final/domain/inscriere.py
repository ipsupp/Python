class Inscriere:

    def __init__(self, idInscriere, idPersoana, idEveniment):
        self.__idInscriere = idInscriere
        self.__idPersoana = idPersoana
        self.__idEveniment = idEveniment

    def get_idInscriere(self):
        return self.__idInscriere

    def get_idPersoana_i(self):
        return self.__idPersoana

    def get_idEveniment_i(self):
        return self.__idEveniment

    def set_idInscriere(self, idInscriere):
        self.__idInscriere = idInscriere

    def set_idPersoana_i(self, idPersoana):
        self.__idPersoana = idPersoana

    def set_idEveniment_i(self, idEveniment):
        self.__idEveniment = idEveniment

    def __str__(self):
        return f' ID_Inscriere: {self.__idInscriere}, ID_Persoana: {self.__idPersoana}, ID_Eveniment: {self.__idEveniment}'