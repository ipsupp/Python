from unittest import TestCase

from domain.entity import Entitate
from domain.eveniment import Eveniment
from domain.inscriere import Inscriere
from domain.persoana import Persoana
from repositories.evenimentRepository import EvenimentRepository
from repositories.inscriereRepository import InscriereRepository
from repositories.persoanaRepository import PersoanaRepository
from service.evenimentService import EvenimentService
from service.inscriereService import InscriereService
from service.persoanaService import PersoanaService
from ui.console import Consola


#id, nume, adresa, participari
class TestPersoana(TestCase):
    def setUp(self):
        self.persoana = Persoana(1, "Ana", "Venus", 2)

    def test_id(self):
        self.assertTrue(self.persoana.get_idPersoana() == 1)
        self.persoana.set_idPersoana(2)
        self.assertTrue(self.persoana.get_idPersoana() == 2)

    def test_nume(self):
        self.assertTrue(self.persoana.get_nume() == "Ana")
        self.persoana.set_nume("Anna")
        self.assertTrue(self.persoana.get_nume() == "Anna")

    def test_adresa(self):
        self.assertTrue(self.persoana.get_adresa() == "Venus")
        self.persoana.set_adresa("Jupiter")
        self.assertTrue(self.persoana.get_adresa() == "Jupiter")

    def test_participari(self):
        self.assertTrue(self.persoana.get_participari() == 2)
        self.persoana.set_participari(1)
        self.assertTrue(self.persoana.get_participari() == 1)

    def test_str(self):
        self.assertTrue(self.persoana.__str__() == f'ID_Persoana: {self.persoana.get_idPersoana()}, Nume: {self.persoana.get_nume()}, Adresa: {self.persoana.get_adresa()}, NrParticipari: {self.persoana.get_participari()} ')

    def tearDown(self) -> None:
        pass

class TestPersoanaService(TestCase):
    def setUp(self) -> None:
        self.persoanaRepository = PersoanaRepository()
        self.evenimentRepository = EvenimentRepository()
        self.inscriereRepository = InscriereRepository(self.persoanaRepository,self.evenimentRepository)
        self.persoanaService = PersoanaService(self.persoanaRepository, self.inscriereRepository)
        self.persoane = []

    def test_get_all(self):
        self.persoanaService.adauga(1, "Ana", "Jupiter", 2)
        self.persoanaService.adauga(2, "Bella", "Venus", 3)
        persoane = self.persoanaService.get_all()
        self.assertTrue(persoane[0].get_idPersoana() == 1)
        self.assertTrue(persoane[1].get_idPersoana() == 2)

    def test_adauga(self):
        self.persoanaService.adauga(1, "Ana", "Jupiter", 2)
        self.persoanaService.adauga(2, "Bella", "Venus", 3)
        persoane = self.persoanaService.get_all()
        self.assertTrue(len(persoane) == 2)
        self.assertTrue(persoane[0].get_idPersoana() == 1)
        self.assertTrue(persoane[1].get_idPersoana() == 2)

    def test_modifica(self):
        self.persoanaService.adauga(1, "Ana", "Jupiter", 2)
        self.persoanaService.adauga(2, "Bella", "Venus", 3)
        self.persoanaService.modifica(2, "Andrei", "Lalele", 0)
        persoane = self.persoanaService.get_all()
        self.assertTrue(len(persoane) == 2)
        self.assertTrue(persoane[1].get_idPersoana() == 2)
        self.assertTrue(persoane[1].get_nume() == "Andrei")
        self.assertTrue(persoane[1].get_adresa() == "Lalele")
        self.assertTrue(persoane[1].get_participari() == 0)

    def test_sterge(self):
        self.persoanaService.adauga(1, "Ana", "Jupiter", 2)
        self.persoanaService.adauga(2, "Bella", "Venus", 3)
        self.persoanaService.sterge(1)
        persoane = self.persoanaService.get_all()
        self.assertTrue(len(persoane) == 1)
        self.assertTrue(persoane[0].get_idPersoana() == 2)
        self.assertTrue(persoane[0].get_nume() == "Bella")
        self.assertTrue(persoane[0].get_adresa() == "Venus")
        self.assertTrue(persoane[0].get_participari() == 3)

    def test_cauta(self):
        self.persoanaService.adauga(1, "Ana", "Jupiter", 2)
        self.persoanaService.adauga(2, "Bella", "Venus", 3)
        self.persoanaService.adauga(3, "Dan", "Motilor", 1)
        persoane = self.persoanaService.get_all()
        aux = self.persoanaService.cauta(persoane[0].get_idPersoana())
        self.assertTrue(aux == persoane[0])


    def tearDown(self) -> None:
        pass

class TestPersoanaRepository(TestCase):
    def setUp(self) -> None:
        self.persoanaRepository = PersoanaRepository()
        self.persoane = []

    def test_adauga_error(self):
        self.assertRaises(AttributeError, self.persoanaRepository.adauga_persoana, 'Exista deja persoana cu id-ul dat!')

    def test_modifica_error(self):
        self.assertRaises(AttributeError, self.persoanaRepository.modifica_persoana, 'Nu exista persoana cu id-ul dat!')

    def test_sterge_error(self):
        self.assertRaises(KeyError, self.persoanaRepository.sterge_persoana, 'Nu exista persoana cu id-ul dat!')

    def tearDown(self) -> None:
        pass

class TestEveniment(TestCase):
    def setUp(self) -> None:
        self.eveniment = Eveniment(1,10,100,"a",1)

    def test_id(self):
        self.assertTrue(self.eveniment.get_idEveniment() == 1)
        self.eveniment.set_idEveniment(2)
        self.assertTrue(self.eveniment.get_idEveniment() == 2)

    def test_data(self):
        self.assertTrue(self.eveniment.get_data() == 10)
        self.eveniment.set_data(20)
        self.assertTrue(self.eveniment.get_data() == 20)

    def test_timp(self):
        self.assertTrue(self.eveniment.get_timp() == 100)
        self.eveniment.set_timp(200)
        self.assertTrue(self.eveniment.get_timp() == 200)

    def test_descriere(self):
        self.assertTrue(self.eveniment.get_descriere() == "a")
        self.eveniment.set_descriere("b")
        self.assertTrue(self.eveniment.get_descriere() == "b")

    def test_participanti(self):
        self.assertTrue(self.eveniment.get_participanti() == 1)
        self.eveniment.set_participanti(2)
        self.assertTrue(self.eveniment.get_participanti() == 2)

    def test_str(self):
        self.assertTrue(self.eveniment.__str__() == f' ID_Eveniment: {self.eveniment.get_idEveniment()}, Data: {self.eveniment.get_data()}, Timp: {self.eveniment.get_timp()}, Descriere: {self.eveniment.get_descriere()}, Nr_Participanti: {self.eveniment.get_participanti()}')

class TestEvenimentService(TestCase):
    def setUp(self) -> None:
        self.evenimentRepository = EvenimentRepository()
        self.persoanaRepository = PersoanaRepository()
        self.inscriereRepository = InscriereRepository(self.persoanaRepository,self.evenimentRepository)
        self.evenimentService = EvenimentService(self.evenimentRepository,self.inscriereRepository)
        self.evenimente = []

    def test_get_all(self):
        self.evenimentService.adauga(1,10,100,"a",1)
        self.evenimentService.adauga(2,20,200,"b",2)
        evenimente = self.evenimentService.get_all()
        self.assertTrue(evenimente[0].get_idEveniment() == 1)
        self.assertTrue(evenimente[1].get_idEveniment() == 2)

    def test_adauga(self):
        self.evenimentService.adauga(1, 10, 100, "a", 1)
        self.evenimentService.adauga(2, 20, 200, "b", 2)
        evenimente = self.evenimentService.get_all()
        self.assertTrue(len(evenimente) == 2)
        self.assertTrue(evenimente[0].get_idEveniment() == 1)
        self.assertTrue(evenimente[1].get_idEveniment() == 2)

    def test_modifica(self):
        self.evenimentService.adauga(1, 10, 100, "a", 1)
        self.evenimentService.adauga(2, 20, 200, "b", 2)
        self.evenimentService.modifica(2,21,210,"c",3)
        evenimente = self.evenimentService.get_all()
        self.assertTrue(evenimente[0].get_idEveniment() == 1)
        self.assertTrue(evenimente[1].get_idEveniment() == 2)
        self.assertTrue(evenimente[1].get_data() == 21)
        self.assertTrue(evenimente[1].get_timp() == 210)
        self.assertTrue(evenimente[1].get_descriere() == "c")
        self.assertTrue(evenimente[1].get_participanti() == 3)

    def test_sterge(self):
        self.evenimentService.adauga(1, 10, 100, "a", 1)
        self.evenimentService.adauga(2, 20, 200, "b", 2)
        self.evenimentService.sterge(1)
        evenimente = self.evenimentService.get_all()
        self.assertTrue(evenimente[0].get_idEveniment() == 2)
        self.assertTrue(evenimente[0].get_data() == 20)
        self.assertTrue(evenimente[0].get_timp() == 200)
        self.assertTrue(evenimente[0].get_descriere() == "b")
        self.assertTrue(evenimente[0].get_participanti() == 2)

    def test_cauta(self):
        self.evenimentService.adauga(1, 10, 100, "a", 1)
        self.evenimentService.adauga(2, 20, 200, "b", 2)
        self.evenimentService.adauga(3, 30, 300, "c", 0)
        evenimente = self.evenimentService.get_all()
        aux = self.evenimentService.cauta(evenimente[0].get_idEveniment())
        self.assertTrue(aux == evenimente[0])


    def tearDown(self) -> None:
        pass

class TestEvenimentRepository(TestCase):
    def setUp(self) -> None:
        self.evenimentRepository = EvenimentRepository()
        self.evenimente = []

    def test_adauga_error(self):
        self.assertRaises(AttributeError, self.evenimentRepository.adauga_eveniment, 'Exista deja un eveniment cu id-ul dat!')

    def test_modifica_error(self):
        self.assertRaises(AttributeError, self.evenimentRepository.modifica_eveniment, 'Nu exista eveniment cu id-ul dat!')

    def test_sterge_error(self):
        self.assertRaises(KeyError, self.evenimentRepository.sterge_eveniment, 'Nu exista eveniment cu id-ul dat!')

    def tearDown(self) -> None:
        pass

class TestInscriere(TestCase):
    def setUp(self) -> None:
        self.inscriere = Inscriere(1,2,3)

    def test_id(self):
        self.assertTrue(self.inscriere.get_idInscriere() == 1)
        self.inscriere.set_idInscriere(2)
        self.assertTrue(self.inscriere.get_idInscriere() == 2)

    def test_idPersoana(self):
            self.assertTrue(self.inscriere.get_idPersoana_i() == 2)
            self.inscriere.set_idPersoana_i(3)
            self.assertTrue(self.inscriere.get_idPersoana_i() == 3)

    def test_idEveniment(self):
        self.assertTrue(self.inscriere.get_idEveniment_i() == 3)
        self.inscriere.set_idEveniment_i(4)
        self.assertTrue(self.inscriere.get_idEveniment_i() == 4)

    def test_str(self):
        self.assertTrue(self.inscriere.__str__() == f' ID_Inscriere: {self.inscriere.get_idInscriere()}, ID_Persoana: {self.inscriere.get_idPersoana_i()}, ID_Eveniment: {self.inscriere.get_idEveniment_i()}')

class TestInscriereService(TestCase):
    def setUp(self) -> None:
        self.evenimentRepository = EvenimentRepository()
        self.persoanaRepository = PersoanaRepository()
        self.inscriereRepository = InscriereRepository(self.persoanaRepository, self.evenimentRepository)
        self.persoanaService = PersoanaService(self.persoanaRepository, self.inscriereRepository)
        self.evenimentService = EvenimentService(self.evenimentRepository, self.inscriereRepository)
        self.inscriereService = InscriereService(self.inscriereRepository, self.persoanaRepository, self.evenimentRepository)
        self.inscrieri = []

    def test_get_all(self):
        self.persoanaService.adauga(2, "A", "B", 0)
        self.persoanaService.adauga(3, "C", "D", 0)
        self.evenimentService.adauga(3, 30, 300, "a", 0)
        self.evenimentService.adauga(1, 10, 100, "b", 0)
        self.inscriereService.adauga(1, 2, 3)
        self.inscriereService.adauga(2, 3, 1)
        inscrieri = self.inscriereService.get_all()
        self.assertTrue(inscrieri[0].get_idInscriere() == 1)
        self.assertTrue(inscrieri[1].get_idInscriere() == 2)

    def test_adauga(self):
        self.persoanaService.adauga(2,"A","B",0)
        self.persoanaService.adauga(3,"C","D",0)
        self.evenimentService.adauga(3,30,300,"a",0)
        self.evenimentService.adauga(1,10,100,"b",0)
        self.inscriereService.adauga(1,2,3)
        self.inscriereService.adauga(2,3,1)
        inscrieri = self.inscriereService.get_all()
        self.assertTrue(inscrieri[0].get_idInscriere() == 1)
        self.assertTrue(inscrieri[1].get_idInscriere() == 2)

    def test_sterge(self):
        self.persoanaService.adauga(2, "A", "B", 0)
        self.persoanaService.adauga(3, "C", "D", 0)
        self.evenimentService.adauga(3, 30, 300, "a", 0)
        self.evenimentService.adauga(1, 10, 100, "b", 0)
        self.inscriereService.adauga(1, 2, 3)
        self.inscriereService.adauga(2, 3, 1)
        self.inscriereService.adauga(3, 3 ,3)
        self.inscriereService.sterge(2,3)
        inscrieri = self.inscriereService.get_all()
        self.assertTrue(len(inscrieri) == 2)
        self.assertTrue(inscrieri[0].get_idInscriere() == 2)
        self.assertTrue(inscrieri[0].get_idPersoana_i() == 3)
        self.assertTrue(inscrieri[0].get_idEveniment_i() == 1)

    def test_top_participari(self):
        self.persoanaService.adauga(2, "A", "B", 0)
        self.persoanaService.adauga(3, "C", "D", 0)
        self.evenimentService.adauga(3, 30, 300, "a", 0)
        self.evenimentService.adauga(1, 10, 100, "b", 0)
        self.inscriereService.adauga(1, 2, 3)
        self.inscriereService.adauga(2, 3, 1)
        self.inscriereService.adauga(3, 3, 3)
        persoane = self.persoanaService.get_all()
        rezultat = self.persoanaRepository.top_participari(persoane)
        self.assertTrue(rezultat[0].get_participari() == 2)

    def test_sterge_persoana(self):
        self.persoanaService.adauga(2, "A", "B", 0)
        self.persoanaService.adauga(3, "C", "D", 0)
        self.evenimentService.adauga(3, 30, 300, "a", 0)
        self.evenimentService.adauga(1, 10, 100, "b", 0)
        self.inscriereService.adauga(1, 2, 3)
        self.inscriereService.adauga(2, 3, 1)
        self.inscriereService.adauga(3, 3, 3)
        self.persoanaService.sterge(3)
        persoane = self.persoanaService.get_all()
        self.assertTrue(persoane[0].get_idPersoana() == 2)



    def tearDown(self) -> None:
        pass

class TestInscrieriRepository(TestCase):
    def setUp(self) -> None:
        self.persoanaRepository = PersoanaRepository()
        self.evenimentRepository = EvenimentRepository()
        self.inscriereRepository = InscriereRepository(self.persoanaRepository, self.evenimentRepository)
        self.inscrieri = []

    def test_adauga_error(self):
        self.assertRaises(AttributeError, self.inscriereRepository.adauga_inscriere, 'Exista deja persoana cu id-ul dat!')

    def test_sterge_error(self):
        self.assertRaises(TypeError, self.inscriereRepository.sterge_inscriere, 'Nu exista persoana cu id-ul dat!')

    def tearDown(self) -> None:
        pass

class TestEntitate(TestCase):
    def setUp(self) -> None:
        self.entitate = Entitate(1)

    def test_entitate(self):
        self.assertTrue(self.entitate.get_idEntitate() == 1)
        self.entitate.set_idEntitate(2)
        self.assertTrue(self.entitate.get_idEntitate() == 2)

class TestPersoanaUI(TestCase):
    def setUp(self) -> None:
        self.persoanaRepository = PersoanaRepository()
        self.evenimentRepository = EvenimentRepository()
        self.inscriereRepository = InscriereRepository(self.persoanaRepository, self.evenimentRepository)
        self.persoanaService = PersoanaService(self.persoanaRepository, self.inscriereRepository)
        self.evenimentService = EvenimentService(self.evenimentRepository, self.inscriereRepository)
        self.inscriereService = InscriereService(self.inscriereRepository, self.persoanaRepository,
                                                 self.evenimentRepository)
        self.console = Consola(self.persoanaService,self.evenimentService,self.inscriereService)

    def tearDown(self) -> None:
        pass
