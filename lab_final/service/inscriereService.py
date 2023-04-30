from domain.inscriere import Inscriere
from domain.inscriereDTOdata import InscriereDTODataAssembler
from domain.inscrieriDTOdescriere import InscriereDTODescriereAssembler
from repositories.evenimentRepository import EvenimentRepository
from repositories.inscriereRepository import InscriereRepository
from repositories.persoanaRepository import PersoanaRepository


class InscriereService:
    def __init__(self, inscriereRepository: InscriereRepository, persoanaRepository: PersoanaRepository, evenimentRepository: EvenimentRepository):
        self.__inscriereRepository = inscriereRepository
        self.__persoanaRepository = persoanaRepository
        self.__evenimentRepository = evenimentRepository

    def get_all(self):
        '''
        returneaza lista cu toate inscrierile
        :return: lista inscrieri
        '''
        return self.__inscriereRepository.get_all_inscrieri()

    def adauga(self, idInscriere, idPersoana, idEveniment):
        '''
        adauga in lista o inscriere
        :param idInscriere: str
        :param idPersoana: str
        :param idEveniment: str
        :return:
        '''
        if self.__persoanaRepository.get_by_idPersoana(idPersoana) is None:
            raise KeyError("Nu exista o persoana cu id-ul dat!")
        if self.__evenimentRepository.get_by_idEveniment(idEveniment) is None:
            raise KeyError("Nu exista un eveniment cu id-ul dat!")
        inscrieri = self.__inscriereRepository.get_all_inscrieri()
        for inscriere in inscrieri:
            if inscriere.get_idPersoana_i() == idPersoana and inscriere.get_idEveniment_i() == idEveniment:
                raise ValueError("Persoana este deja inscrisa la acest eveniment!")
        inscriere = Inscriere(idInscriere, idPersoana, idEveniment)
        self.__inscriereRepository.adauga_inscriere(inscriere)

    def sterge(self, idPersoana, idEveniment):
        '''
        sterge o inscriere dupa idPersoana si idEveniment
        :param idPersoana: str
        :param idEveniment: str
        :return:
        '''
        self.__inscriereRepository.sterge_inscriere(idPersoana, idEveniment)

    def creare_DTO_De(self):
        '''
        creeaza o lista cu obiecte de tip InscriereDTODescriere
        :return: lista
        '''
        l = []
        inscrieri = self.get_all()
        for inscriere in inscrieri:
            persoana = self.__persoanaRepository.get_by_idPersoana(inscriere.get_idPersoana_i())
            eveniment = self.__evenimentRepository.get_by_idEveniment(inscriere.get_idEveniment_i())
            descriereEveniment = eveniment.get_descriere()
            iDTO = InscriereDTODescriereAssembler.creeaza_obiect(eveniment, persoana, descriereEveniment)
            l.append(iDTO)
        return l

    def creare_DTO_Da(self):
        '''
        creeaza o lista cu obiecte de tip InscriereDTODescriere
        :return: lista
        '''
        l = []
        inscrieri = self.get_all()
        for inscriere in inscrieri:
            persoana = self.__persoanaRepository.get_by_idPersoana(inscriere.get_idPersoana_i())
            eveniment = self.__evenimentRepository.get_by_idEveniment(inscriere.get_idEveniment_i())
            dataEveniment = eveniment.get_data()
            iDTO = InscriereDTODataAssembler.creeaza_obiect(eveniment, persoana, dataEveniment)
            l.append(iDTO)
        return l

    def sortare_inscrieri_dupa_descriere_DTO(self):
        '''
        sorteaza  dupa descriere
        :return:
        '''
        l = self.creare_DTO_De()
        l.sort(key = lambda ev: ev.descriereEveniment)
        return l

    def sortare_inscrieri_dupa_data_DTO(self):
        '''
        sorteaza dupa data
        :return:
        '''
        l = self.creare_DTO_Da()
        l.sort(key = lambda ev: ev.dataEveniment)
        return l




    #def ordonare_dupa_descriere(self):

        #return self.__evenimentRepository.sortare_dupa_descriere()

    #def ordonare_dupa_data(self):

        #return self.__evenimentRepository.sortare_dupa_data()

