class Eveniment:
    def __init__(self, idEveniment, data, timp, descriere, participanti):
        self.__idEveniment = idEveniment
        self.__data = data
        self.__timp = timp
        self.__descriere = descriere
        self.__participanti = participanti

    def get_idEveniment(self):
        return self.__idEveniment

    def get_data(self):
        return self.__data

    def get_timp(self):
        return self.__timp

    def get_descriere(self):
        return self.__descriere

    def get_participanti(self):
        return self.__participanti

    def set_idEveniment(self, idEveniment):
        self.__idEveniment = idEveniment

    def set_data(self, data):
        self.__data = data

    def set_timp(self, timp):
        self.__timp = timp

    def set_descriere(self, descriere):
        self.__descriere = descriere

    def set_participanti(self, participanti):
        self.__participanti = participanti

    def __str__(self):
        return f' ID_Eveniment: {self.__idEveniment}, Data: {self.__data}, Timp: {self.__timp}, Descriere: {self.__descriere}, Nr_Participanti: {self.__participanti}'
