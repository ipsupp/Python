from domain.eveniment import Eveniment
from repositories.evenimentRepository import EvenimentRepository
from repositories.inscriereRepository import InscriereRepository


class EvenimentService:
    def __init__(self, evenimentRepository: EvenimentRepository, inscriereRepository: InscriereRepository):
        self.__evenimentRepository = evenimentRepository
        self.__inscriereRepository = inscriereRepository

    def get_all(self):
        '''
        returneaza lista de evenimente
        :return: lista de obiecte
        '''
        return self.__evenimentRepository.get_all_evenimente()

    def adauga(self, idEveniment, data, timp, descriere, participanti):
        '''
        adauga un eveniment
        :param idEveniment: str
        :param data: int
        :param timp: int
        :param descriere: str
        :param participanti: int
        :return:
        '''
        eveniment = Eveniment(idEveniment, data, timp, descriere, participanti)
        self.__evenimentRepository.adauga_eveniment(eveniment)

    def modifica(self, idEveniment, dataNew, timpNew, descriereNew, participanti):
        '''
        modifica un eveniment
        :param idEveniment: str
        :param dataNew: int
        :param timpNew: int
        :param descriereNew: str
        :param participanti: int
        :return:
        '''
        evenimentNew = Eveniment(idEveniment, dataNew, timpNew, descriereNew, participanti)
        self.__evenimentRepository.modifica_eveniment(evenimentNew)

    def sterge(self, idEveniment):
        '''
        sterge eveniment dupa id
        :param idEveniment: str
        :return:
        '''
        inscrieri = self.__inscriereRepository.get_all_inscrieri()

        for inscriere in inscrieri:
            if inscriere.get_idEveniment_i() == idEveniment:
                id = inscriere.get_idPersoana_i()
                self.__inscriereRepository.sterge_inscriere(id, idEveniment)
        self.__evenimentRepository.sterge_eveniment(idEveniment)

    def cauta(self, idEveniment):
        '''
        cauta un eveniment dupa id
        :param idEveniment: str
        :return:
        '''
        aux = self.__evenimentRepository.cautare_eveniment(idEveniment)
        if aux == None:
            raise Exception("Nu exista acest eveniment!")
        else:
            return aux

    def top20_dupa_participanti(self):
        '''
        returneaza top 20 evenimente dupa participanti
        :return:lista sortata
        '''
        return self.__evenimentRepository.top20_participari()

