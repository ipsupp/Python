from domain.persoana import Persoana
from repositories.persoanaRepository import PersoanaRepository


class PersoanaFileRepository(PersoanaRepository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__readFile()

    def adauga(self, persoana):
        super().adauga_persoana(persoana)
        self.__writeFile()

    def modifica(self, persoanaNew):
        super().modifica_persoana(persoanaNew)
        self.__writeFile()

    def sterge(self, idPersoana):
        super().sterge_persoana(idPersoana)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:

                idPersoana = line.split()[0]
                nume = line.split()[1]
                adresa = line.split()[2]
                participari = 0


                persoana = Persoana(idPersoana, nume, adresa, participari)
                super().adauga_persoana(persoana)

            f.close()
    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for persoana in self.get_all_persoane():
                f.write(f'{persoana.get_idEntitate()} {persoana.get_nume()} {persoana.get_adresa()} \n')


