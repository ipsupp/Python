from domain.persoana import Persoana
from repositories.inscriereRepository import InscriereRepository
from repositories.persoanaRepository import PersoanaRepository


class PersoanaService:
    def __init__(self, persoanaRepository: PersoanaRepository, inscriereRepository: InscriereRepository):
        self.__persoanaRepository = persoanaRepository
        self.__inscriereRepository = inscriereRepository

    def get_all(self):
        '''
        returneaza o lista cu toate persoanele
        :return: lista de persoane
        '''
        return self.__persoanaRepository.get_all_persoane()

    def adauga(self, idPersoana, nume, adresa, participari):
        '''
        adauga in lista o persoana
        :param idPersoana: str
        :param nume: str
        :param adresa: str
        :param participari: int
        :return:
        '''
        persoana = Persoana(idPersoana, nume, adresa, participari)
        self.__persoanaRepository.adauga_persoana(persoana)

    def modifica(self, idPersoana, numeNew, adresaNew, participari):
        '''
        modifica in lista o persoana
        :param idPersoana: str
        :param numeNew: str
        :param adresaNew: str
        :param participari: int
        :return:
        '''
        persoanaNew = Persoana(idPersoana, numeNew, adresaNew, participari)
        self.__persoanaRepository.modifica_persoana(persoanaNew)

    def sterge(self, idPersoana):
        '''
        sterge din lista o persoana
        :param idPersoana: str
        :return:
        '''
        inscrieri = self.__inscriereRepository.get_all_inscrieri()
        for inscriere in inscrieri:
            if inscriere.get_idPersoana_i() == idPersoana:
                id = inscriere.get_idEveniment_i()
                self.__inscriereRepository.sterge_inscriere(idPersoana, id)
        self.__persoanaRepository.sterge_persoana(idPersoana)

    def cauta(self, idPersoana):
        '''
        cauta o persoana dupa id
        :param idPersoana: str
        :return: persoana
        '''
        aux= self.__persoanaRepository.cautare_persoana(idPersoana)
        if aux == None:
            raise KeyError("Nu exista aceasta persoana!")
        else:
            return aux

    def top_participari(self):
        '''
        returneaza lista cu persoane / persoana care au nr maxim de participari
        :return: lista
        '''
        persoane = self.__persoanaRepository.get_all_persoane()
        return self.__persoanaRepository.top_participari(persoane)