
class PersoanaRepository:
    def __init__(self):
        self.__persoane = {}

    def get_all_persoane(self):
        '''
        returneaza lista de persoana
        :return:lista de obiecte
        '''
        return list(self.__persoane.values())

    def get_by_idPersoana(self, idPersoana):
        '''
        retuneaza o persoana dupa id
        :param idPersoana: str
        :return: obiect de tip persoana
        '''
        persoane = self.get_all_persoane()
        for persoana in persoane:
            if persoana.get_idPersoana() == idPersoana:
                return persoana
        return None

    def adauga_persoana(self, persoana):
        '''
        adauga o persoana in lista
        :param persoana: obiect de tip persoana
        :return:
        '''
        if self.get_by_idPersoana(persoana.get_idPersoana()) is not None:
            raise KeyError("Exista deja persoana cu id-ul dat!")
        self.__persoane[persoana.get_idPersoana()] = persoana

    def modifica_persoana(self, persoanaNew):
        '''
        modifica o persoana din lista
        :param persoanaNew: obiect de tip persoana
        :return:
        '''
        if self.get_by_idPersoana(persoanaNew.get_idPersoana()) is None:
            raise KeyError("Nu exista persoana cu id-ul dat!")
        self.__persoane[persoanaNew.get_idPersoana()] = persoanaNew

    def sterge_persoana(self, idPersoana):
        '''
        sterge o persoana din lista dupa id
        :param idPersoana: str
        :return:
        '''
        if self.get_by_idPersoana(idPersoana) is None:
            raise KeyError("Nu exista persoana cu id-ul dat!")
        self.__persoane.pop(idPersoana)

    def nr_persoane(self):
        '''
        returneaza nr de persoane
        :return: nr de persoane
        '''
        return int(len(self.__persoane))

    def participari_plus(self, idPersoana):
        '''
        creste var participari cu 1 dupa id
        :param idPersoana: str
        :return:
        '''
        if self.get_by_idPersoana(idPersoana) is None:
            raise ValueError ("Nu exista persoana cu acest id!")
        entitate =  self.get_by_idPersoana(idPersoana)
        part = int(entitate.get_participari())
        self.get_by_idPersoana(idPersoana).set_participari(part + 1)
###
    def participari_minus(self, idPersoana):
        '''
        scade var participari cu 1 dupa id
        :param idPersoana: str
        :return:
        '''
        if self.get_by_idPersoana(idPersoana) is None:
            raise ValueError ("Nu exista persoana cu acest id!")
        entitate = self.get_by_idPersoana(idPersoana)
        part = int(entitate.get_participari())
        self.get_by_idPersoana(idPersoana).set_participari(part - 1)

    def sortare_dupa_participari(self):
        '''
        returneaza lista de persoane sortata dupa participari
        :return:  lista de persoane sortata dupa participari
        '''
        return sorted(self.__persoane.values(), key = lambda x: x.get_participari, reverse = True)

    def top_participari(self,persoane):
        '''
        returneaza persoanele / persoana cu cele mai multe participari
        :param persoane: lista de obiecte tip persoana
        :return: lista sortata
        '''
        maxx = 0
        lst = []
        for persoana in persoane:
            if persoana.get_participari() > maxx:
                maxx = int(persoana.get_participari())

        for persoana in persoane:
            if persoana.get_participari() == maxx:
                lst.append(persoana)
        return lst

    def cautare_persoana(self, idPersoana):
        '''
        cauta persoana dupa id
        :param idPersoana: str
        :return: obiect tip persoana daca exista, altfel None
        '''
        persoane = self.get_all_persoane()
        for persoana in persoane:
            if persoana.get_idPersoana() == idPersoana:
                return persoana
        return None
