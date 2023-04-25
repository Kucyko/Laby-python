class Sklep:
    def wypiszcene(self,piwo):
        x=self.nazwa.index(piwo)
        j=self.nazwa[x]
        y=self.cena[x]
        print("Cena dla piwa: "+ str(j) +" to: "+ str(y))




class Beer:
    def __init__(self,nazwa,rodzaj,procenty,ocena,opinia):
        self.nazwa = nazwa
        self.rodzaj = rodzaj
        self.procenty = procenty
        self.ocena = ocena
        self.opinia = opinia

    def nazwaa(self,piwo):
        piwa = [piwo1,piwo2,piwo3]
        for p in piwa:
            print("Nazwa:", p.nazwa)
            print("Rodzaj:", p.rodzaj)
            print("Procenty:", p.procenty)
            print("Ocena:", p.ocena)
            print("Opinia:", p.opinia)
            print()
    def sortuj(self):
        piwa = [piwo1,piwo2,piwo3]
        posortowane_piwa = sorted(piwa, key=lambda p: p.ocena, reverse=True)
        for p in posortowane_piwa:
            print("Nazwa:", p.nazwa)
            print("Rodzaj:", p.rodzaj)
            print("Procenty:", p.procenty)
            print("Ocena:", p.ocena)
            print("Opinia:", p.opinia)
            print()
piwo=Beer


piwo1 = piwo("lech","jasne","5%",4.0,"dobre")
piwo2 = piwo("kozel","ciemne","4%",5.0,"świetne")
piwo3 = piwo("tyskie","białe","3%",3.0,"ściek")

piwo1.nazwaa("kozel")
piwo1.sortuj()