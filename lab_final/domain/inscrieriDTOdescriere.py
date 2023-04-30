from dataclasses import dataclass


@dataclass
class InscriereDTODescriere:
    durataEveniment: str
    numePersoana: str
    descriereEveniment: str

class InscriereDTODescriereAssembler:
    @staticmethod
    def creeaza_obiect(eveniment, persoana, descriereEveniment):
        durataEveniment = eveniment.get_timp()
        numePersoana = persoana.get_nume()
        return InscriereDTODescriere(durataEveniment, numePersoana, descriereEveniment)
