from repositories.evenimentFileRepository import EvenimentFileRepository
from repositories.inscriereFileRepository import InscriereFileRepository
from repositories.persoanaFileRepository import PersoanaFileRepository
from service.evenimentService import EvenimentService
from service.inscriereService import InscriereService
from service.persoanaService import PersoanaService
from ui.console import Consola


def main():
    #test_all()
    persoanaRepository = PersoanaFileRepository("files/persoane.txt")
    evenimentRepository = EvenimentFileRepository("files/evenimente.txt")
    inscriereRepository = InscriereFileRepository("files/inscrieri.txt", persoanaRepository, evenimentRepository)

    persoanaService = PersoanaService(persoanaRepository, inscriereRepository)
    evenimentService = EvenimentService(evenimentRepository, inscriereRepository)
    inscriereService = InscriereService(inscriereRepository, persoanaRepository, evenimentRepository)

    consola = Consola(persoanaService, evenimentService, inscriereService)
    consola.main_meniu()

main()
