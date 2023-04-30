from service.evenimentService import EvenimentService
from service.inscriereService import InscriereService
from service.persoanaService import PersoanaService


class Consola:
    def __init__(self, persoanaService: PersoanaService, evenimentService: EvenimentService, inscriereService: InscriereService):
        self.__persoanaService = persoanaService
        self.__evenimentService = evenimentService
        self.__inscriereService = inscriereService

    def afisare(self,entitati):
        for entitate in entitati:
            print(entitate)
    def adauga_persoana(self):
        try:
            idPersoana = input("Dati ID-ul persoanei: ")
            nume = input("Dati numele persoanei: ")
            adresa = input("Dati adresa persoanei: ")
            participari = 0
            self.__persoanaService.adauga(idPersoana, nume, adresa, participari)
        except KeyError as error:
            print(error)

    def adauga_eveniment(self):
        try:
            idEveniment = input("Dati id-ul evenimentului: ")
            data = input("Dati data evenimentului: ")
            timp = input("Dati durata in minute ( timp ) a evenimentului: ")
            descriere = input("Dati o descriere evenimentului: ")
            participanti = 0
            self.__evenimentService.adauga(idEveniment, data, timp, descriere, participanti)
        except KeyError as error:
            print(error)

    def adauga_inscriere(self):
        try:
            idPersoanaEveniment = input("Dati un id inscrierii: ")
            idEveniment = input("Dati id-ul evenimentului: ")
            idPersoana = input("Dati id-ul persoanei: ")
            self.__inscriereService.adauga(idPersoanaEveniment, idPersoana, idEveniment)
        except KeyError as error:
            print(error)

    def modifica_persoana(self):
        try:
            idPersoana = input("Dati ID-ul persoanei: ")
            numeNew = input("Dati noul nume al persoanei: ")
            adresaNew = input("Dati noua adresa persoanei: ")
            participari = 0
            self.__persoanaService.modifica(idPersoana, numeNew, adresaNew, participari)
        except KeyError as error:
            print(error)

    def modifica_eveniment(self):
        try:
            idEveniment = input("Dati id-ul evenimentului: ")
            dataNoua = input("Dati noua data a evenimentului: ")
            timpNou = input("Dati noua durata (timpul) a evenimentului: ")
            descriereNoua = input("Dati noua descriere a evenimentului: ")
            participanti = 0
            self.__evenimentService.modifica(idEveniment, dataNoua, timpNou, descriereNoua, participanti)
        except KeyError as error:
            print(error)

    def sterge_persoana(self):
        try:
            idPersoana = input("Dati ID-ul persoanei: ")
            self.__persoanaService.sterge(idPersoana)
        except KeyError as error:
            print(error)

    def sterge_eveniment(self):
        try:
            idEveniment = input("Dati id-ul evenimentului: ")
            self.__evenimentService.sterge(idEveniment)
        except KeyError as error:
            print(error)

    def sterge_inscriere(self):
        try:
            idPersoana = input("Dati id-ul persoanei: ")
            idEveniment = input("Dati id-ul evenimentului: ")
            self.__inscriereService.sterge(idPersoana, idEveniment)
        except KeyError as error:
            print(error)

    def cautare_persoana(self):
        try:
            idPersoana = input("Dati id-ul persoanei: ")
            aux = self.__persoanaService.cauta(idPersoana)
            print(aux)
        except KeyError as error:
            print(error)

    def cautare_eveniment(self):
        try:
            idEveniment = input("Dati id-ul evenimentului: ")
            aux = self.__evenimentService.cauta(idEveniment)
            print(aux)
        except KeyError as error:
            print(error)

    def sortare_inscriere_descriere(self):
        rezultat = self.__inscriereService.sortare_inscrieri_dupa_descriere_DTO()
        for obj in rezultat:
           print  (f'Descriere: {obj.descriereEveniment}, Durata_Eveniment: {obj.durataEveniment} ,Nume_Persoana: {obj.numePersoana}')

    def sortare_inscriere_data(self):
        rezultat = self.__inscriereService.sortare_inscrieri_dupa_data_DTO()
        for obj in rezultat:
            print(f'Data: {obj.dataEveniment}, Nume_Persoana: {obj.numePersoana}, Desc_Eveniment: {obj.descriereEveniment}')

    '''
    def ordonare_persoana_data_DTO(self):
        rezultat = self.__inscriereService.ordonare_dupa_data()
        self.afisare(rezultat)

    def ordonare_dupa_descriere_DTO(self):
        rezultat = self.__inscriereService.ordonare_dupa_descriere()
        self.afisare(rezultat)
    '''
    def top_participare(self):
        rezultat = self.__persoanaService.top_participari()
        self.afisare(rezultat)

    def top20_participanti(self):
        rezultat = self.__evenimentService.top20_dupa_participanti()
        self.afisare(rezultat)

    def menu(self):
        print("1.  Adauga persoana ")
        print("2.  Modifica persoana ")
        print("3.  Sterge persoana ")
        print("4.  Adauga eveniment")
        print("5.  Modifica eveniment")
        print("6.  Sterge eveniment")
        print("7.  Inscriere persoana la eveniment")
        print("8.  Sterge o inscriere")
        print("9.  Cautare persoana")
        print("10. Cautare eveniment")
        print("11. Sortare inscrieri (DTO)")
        print("12. Persoane participante la cele mai multe evenimente")
        print("13. Primele 20% evenimente cu cei mai multi participanti")
        print("a.  Afiseaza toate persoanele")
        print("b.  Afiseaza toate evenimentele")
        print("c.  Afiseaza toate inscrierile")
        print("x.  Iesire ")

    def sub_meniu_ordonari(self):
        print("1. Sorteaza inscrierile dupa descriere (asociata evenimentului) ")
        print("2. Sorteaza inscrierile dupa data (asociata evenimentului) ")

    def main_meniu(self):
        while True:
            self.menu()
            optiune = input("Alegeti optiunea: ")
            if optiune == "1":
                try:
                    self.adauga_persoana()
                except ValueError as error:
                    print(error)
            elif optiune == "2":
                try:
                    self.modifica_persoana()
                except ValueError as error:
                    print(error)
            elif optiune == "3":
                try:
                    self.sterge_persoana()
                except ValueError as error:
                    print(error)
            elif optiune == "4":
                try:
                    self.adauga_eveniment()
                except ValueError as error:
                    print(error)
            elif optiune == "5":
                try:
                    self.modifica_eveniment()
                except ValueError as error:
                    print(error)
            elif optiune == "6":
                try:
                    self.sterge_eveniment()
                except ValueError as error:
                    print(error)
            elif optiune == "7":
                try:
                    self.adauga_inscriere()
                except ValueError as error:
                    print(error)
            elif optiune == "8":
                try:
                    self.sterge_inscriere()
                except ValueError as error:
                    print(error)
            elif optiune == "9":
                try:
                    self.cautare_persoana()
                except ValueError as error:
                    print(error)
            elif optiune == "10":
                try:
                    self.cautare_eveniment()
                except ValueError as error:
                    print(error)
            elif optiune == "11":
                self.sub_meniu_ordonari()
                sub_optiune = input("Alegeti criteriul de sortare: ")
                if sub_optiune == "1":
                    try:
                        self.sortare_inscriere_descriere()
                    except ValueError as error:
                        print(error)
                elif sub_optiune == "2":
                    try:
                        self.sortare_inscriere_data()
                    except ValueError as error:
                        print(error)
            elif optiune == "12":
                try:
                    self.top_participare()
                except ValueError as error:
                    print(error)
            elif optiune == "13":
                try:
                    self.top20_participanti()
                except ValueError as error:
                    print(error)
            elif optiune == "a":
                self.afisare(self.__persoanaService.get_all())
            elif optiune == "b":
                self.afisare(self.__evenimentService.get_all())
            elif optiune == "c":
                self.afisare(self.__inscriereService.get_all())
            elif optiune == "x":
                print("")
                print("Incheiere program.")
                break
            else:
                print("Optiune invalida, reincercati! ")

