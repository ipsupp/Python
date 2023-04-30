from domain.inscriere import Inscriere
from repositories.inscriereRepository import InscriereRepository


class InscriereFileRepository(InscriereRepository):
    def __init__(self, fileName, persoanaFileRepository, evenimentFileRepository):
        super().__init__(persoanaFileRepository, evenimentFileRepository)
        self.__fileName = fileName
        self.__readFile()

    def adauga(self, inscriere):
        super().adauga_inscriere(inscriere)
        self.__writeFile()

    def sterge(self, idPersoana, idEveniment):
        super().sterge_inscriere(idPersoana, idEveniment)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                idInscriere = line.split()[0]
                idPersoana = line.split()[1]
                idEveniment = line.split()[2]

                inscriere = Inscriere(idInscriere, idPersoana, idEveniment)
                super().adauga_inscriere(inscriere)
            f.close()

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for inscriere in self.get_all_inscrieri():
                f.write(f'{inscriere.get_idInscriere()} {inscriere.get_idPersoana_i()} {inscriere.get_idEveniment_i()} \n')


