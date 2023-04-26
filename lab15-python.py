
class Shop:
    def __init__(self,nazwa):
        self.nazwa_sklepu = nazwa
        
    def sprzedaj_piwo(self, piwo):
        print(f"Sprzedano piwo {piwo.nazwa} w sklepie {self.nazwa_sklepu}")





class Beer(Shop):
    piwa = []
    def __init__(self,nazwa,rodzaj,procenty,ocena,opinia):
        super().__init__("Pan Tadzio")
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.procenty = procenty
        self.ocena = ocena
        self.opinia = opinia
        Beer.piwa.append(self)
    @classmethod
    def nazwaa(cls,piwo):
        for p in cls.piwa:
            if p.nazwa == piwo:
                print("Nazwa:", p.nazwa)
                print("Rodzaj:", p.rodzaj)
                print("Procenty:", p.procenty)
                print("Ocena:", p.ocena)
                print("Opinia:", p.opinia)
                print()
                return
    @classmethod     
    def sortuj(cls):
        posortowane_piwa = sorted(cls.piwa, key=lambda p: p.nazwa, reverse=False)
        for p in posortowane_piwa:
            print("Nazwa:", p.nazwa)
            print("Rodzaj:", p.rodzaj)
            print("Procenty:", p.procenty)
            print("Ocena:", p.ocena)
            print("Opinia:", p.opinia)
            print()
    
    def sprzedaj(self):
        super().sprzedaj_piwo(self)
piwo=Beer
sklep=Shop

piwo1 = piwo("lech","jasne","5%",4.0,"dobre")
piwo2 = piwo("kozel","ciemne","4%",5.0,"świetne")
piwo3 = piwo("tyskie","białe","3%",3.0,"ściek")
#Shop.podajsr("piwa")
#Beer.nazwaa("lech")
#Beer.sortuj()
piwo1.sprzedaj()


class Obywatel:
    oby = []
    def __init__(self):
        self.imie = ""
        self.nazwisko = ""
        self.ulica = ""
        self.nrdomu = ""
        self.kodpocztowy = ""
        self.miejscowosc = ""
        Obywatel.oby.append(self)
    def wczytajdane(self):
        self.imie = input("Podaj imię: ")
        self.nazwisko = input("Podaj nazwisko: ")
        self.ulica = input("Podaj ulicę: ")
        self.nrdomu = str(input("Podaj numer domu: "))
        self.kodpocztowy = input("Podaj kod pocztowy: ")
        self.miejscowosc = input("Podaj miejscowość: ")
    @classmethod
    def drukuj(cls,nazwiskoo,nazwa_pliku):
        for p in cls.oby:
            if p.nazwisko == nazwiskoo:
                with open(nazwa_pliku, "w") as f:
                    wizytowka = f"------------- \n {p.imie} {p.nazwisko} \n {p.ulica} {p.nrdomu} \n {p.kodpocztowy} {p.miejscowosc} \n--------------"
                    f.write(wizytowka)
                    print(wizytowka)
jan = Obywatel()
jan.wczytajdane()
jan.drukuj("Kowalczyk","wizytowka1.txt")


class Talia:
    karty = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    kolory = ['kier','karo','trefl','pik']
    def __init__(self,karta,kolor):
        self.karta = karta
        self.kolor = kolor
        Talia.karty.append(self.karta)
        Talia.kolory.append(self.kolor)
    def

karte = Talia


