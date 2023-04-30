from repositories.evenimentRepository import EvenimentRepository
from repositories.persoanaRepository import PersoanaRepository


class InscriereRepository:
    def __init__(self, persoanaRepository: PersoanaRepository, evenimentRepository: EvenimentRepository):
        self.__inscrieri = {}
        self.__evenimentRepository = evenimentRepository
        self.__persoanaRepository = persoanaRepository

    def get_all_inscrieri(self):
        '''
        returneaza lista de inscrieri
        :return: lista de obiecte
        '''
        return list(self.__inscrieri.values())

    def get_by_idInscriere(self, idInscriere):
        '''
        returneaza inscrierea cu id ul dat
        :param idInscriere: str
        :return: obiect de tip inscriere
        '''
        inscrieri = self.get_all_inscrieri()
        for inscriere in inscrieri:
            if inscriere.get_idInscriere == idInscriere:
                return inscriere
        return None

    def adauga_inscriere(self, inscriere):
        '''
        adauga o inscriere in dictionar
        :param inscriere: obiect de tip inscriere
        :return:
        '''
        if self.get_by_idInscriere(inscriere.get_idInscriere()) is not None:
            raise KeyError("Exista deja inscriere cu id-ul dat!")
        self.__inscrieri[inscriere.get_idInscriere()] = inscriere
        self.__evenimentRepository.participanti_plus(inscriere.get_idEveniment_i())
        self.__persoanaRepository.participari_plus(inscriere.get_idPersoana_i())

    def sterge_inscriere(self, idPersoana, idEveniment):
        '''
        sterge o inscriere din dictionar
        :param idPersoana: str
        :param idEveniment: str
        :return:
        '''
        idInscriere = None
        inscrieri = self.get_all_inscrieri()
        for inscriere in inscrieri:
            if inscriere.get_idEveniment_i() == idEveniment and inscriere.get_idPersoana_i() == idPersoana:
                idInscriere = inscriere.get_idInscriere()
        if idInscriere == None:
            raise KeyError("Nu exista inregistrare cu id-ul dat!")
        else:
            self.__evenimentRepository.participanti_minus(idEveniment)
            self.__persoanaRepository.participari_minus(idPersoana)
            self.__inscrieri.pop(idInscriere)
    def nr_inscrieri(self):
        '''
        returneaza nr de inscrieri
        :return: nr de inscrieri
        '''
        return int(len(self.__inscrieri))
