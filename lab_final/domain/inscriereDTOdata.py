from dataclasses import dataclass


@dataclass
class InscriereDTOData:
    descriereEveniment: str
    numePersoana: str
    dataEveniment: str


class InscriereDTODataAssembler:
    @staticmethod
    def creeaza_obiect(eveniment, persoana, dataEveniment):
        descriereEveniment = eveniment.get_descriere()
        numePersoana = persoana.get_nume()
        return InscriereDTOData(descriereEveniment, numePersoana, dataEveniment)
