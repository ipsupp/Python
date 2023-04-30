from domain.eveniment import Eveniment
from repositories.evenimentRepository import EvenimentRepository


class EvenimentFileRepository(EvenimentRepository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__readFile()

    def adauga(self, eveniment):
        super().adauga_eveniment(eveniment)
        self.__writeFile()

    def modifica(self, evenimentNew):
        super().modifica_eveniment(evenimentNew)
        self.__writeFile()

    def sterge(self, idEveniment):
        super().sterge_eveniment(idEveniment)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:

                idEveniment = line.split()[0]
                data = line.split()[1]
                timp = line.split()[2]
                descriere = line.split()[3]
                participanti = 0

                eveniment = Eveniment(idEveniment, data, timp, descriere, participanti)
                super().adauga_eveniment(eveniment)
            f.close()


    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for eveniment in self.get_all_evenimente():
                f.write(f'{eveniment.get_idEntitate()} {eveniment.get_data()} {eveniment.get_timp()} {eveniment.get_descriere()} \n')


