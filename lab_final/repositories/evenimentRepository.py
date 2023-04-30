class EvenimentRepository:
    def __init__(self):
        self.__evenimente = {}

    def get_all_evenimente(self):
        '''
        returneaza lista de evenimente
        :return: lista de obiecte
        '''
        return list(self.__evenimente.values())

    def get_by_idEveniment(self, idEveniment):
        '''
        returneaza evenimentul cu id ul dat
        :param idEveniment: str
        :return: obiect de tip eveniment
        '''
        evenimente = self.get_all_evenimente()
        for eveniment in evenimente:
            if eveniment.get_idEveniment() == idEveniment:
                return eveniment
        return None

    def adauga_eveniment(self, eveniment):
        '''
        adauga un eveniment in dictionar
        :param eveniment: obiect de tip eveniment
        :return:
        '''
        if self.get_by_idEveniment(eveniment.get_idEveniment()) is not None:
            raise KeyError("Exista deja un eveniment cu id-ul dat!")
        self.__evenimente[eveniment.get_idEveniment()] = eveniment

    def modifica_eveniment(self, evenimentNew):
        '''
        modifica un eveniment in dictionar
        :param evenimentNew: obiect de tip eveniment
        :return:
        '''
        if self.get_by_idEveniment(evenimentNew.get_idEveniment()) is None:
            raise KeyError("Nu exista eveniment cu id-ul dat!")
        self.__evenimente[evenimentNew.get_idEveniment()] = evenimentNew

    def sterge_eveniment(self, idEveniment):
        '''
        sterge un eveniment din dictionar
        :param idEveniment: str
        :return:
        '''
        if self.get_by_idEveniment(idEveniment) is None:
            raise KeyError("Nu exista eveniment cu id-ul dat!")
        self.__evenimente.pop(idEveniment)

    def nr_evenimente(self):
        '''
        returneaza nr de evenimente
        :return: nr de evenimente
        '''
        return int(len(self.__evenimente))

    def sortare_dupa_descriere(self):
        '''
        returneaza evenimentele sortate dupa descriere
        :return: lista de evenimente sortata dupa descriere
        '''
        return sorted(self.__evenimente.values(), key=lambda x: x.get_descriere())

    def sortare_dupa_data(self):
        '''
        returneaza evenimentele sortate dupa data
        :return: lista de evenimente sortata dupa data
        '''
        return sorted(self.__evenimente.values(), key=lambda x: x.get_data())

    def sortare_dupa_participanti(self):
        '''
        retuneaza evenimentele sortate dupa nr de participanti
        :return: lista de evenimente sortata dupa nr de participanti
        '''
        return sorted(self.__evenimente.values(), key=lambda x: x.get_participanti(), reverse = True)

    def participanti_plus(self, idEveniment):
        '''
        creste var participanti cu 1 dupa id
        :param idEveniment: str
        :return:
        '''
        if self.get_by_idEveniment(idEveniment) is None:
            raise KeyError("Nu exista un eveniment cu acest id!")
        entitate = self.get_by_idEveniment(idEveniment)
        part = int(entitate.get_participanti())
        self.get_by_idEveniment(idEveniment).set_participanti(part + 1)

    def participanti_minus(self, idEveniment):
        '''
        scade var participanti cu 1 dupa id
        :param idEveniment: str
        :return:
        '''
        if self.get_by_idEveniment(idEveniment) is None:
            raise ValueError("Nu exista un eveniment cu acest id!")
        entitate = self.get_by_idEveniment(idEveniment)
        part = int(entitate.get_participanti())
        self.get_by_idEveniment(idEveniment).set_participanti(part - 1)

    def top20_participari(self):
        '''
        alege evenimentele in top 20, sortate dupa nr de participanti
        :return: top 20 de evenimente sortate dupa nr de participanti
        '''
        lst1 = []
        percent = 0.2
        n = self.nr_evenimente()
        nr = int(percent * n)
        lst2 = self.sortare_dupa_participanti()
        for i in range (nr):
            lst1.append(lst2[i])
        return lst1

    def cautare_eveniment(self, idEveniment):
        '''
        cauta un eveniment dupa id
        :param idEveniment: str
        :return:
        '''
        evenimente = self.get_all_evenimente()
        for eveniment in evenimente:
            if eveniment.get_idEveniment() == idEveniment:
                return eveniment
        return None

