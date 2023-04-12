#1
'''
class Smochod:
    marka="Ferrari"
    model="kabriolet"
    przebieg="100"
    kolor="czerwony"
    wartosc="6000"
    def jedzprosto(self, jazda, prosto):
        return "Samochod jedzie: " + jazda + prosto
    def otwieranydach(self,otwierany):
        return "Czy otwiera sie dach?: "+ otwierany
    def jakszybko(self,szybkosc):
        return "Jak szybko jedzie?: "+ str(szybkosc)
    def dodajPrzebieg(self,przeb):
        return int(self.przebieg) + int(przeb)
obiekt=Smochod()
print(obiekt.jedzprosto("prosto","szybko"))
print(obiekt.otwieranydach("tak"))
print(obiekt.jakszybko("szybko"))
print(obiekt.dodajPrzebieg(1000))
'''
#2
'''
class Ksiazka:
    tytul=[]
    autor=[]
    lstron=[]
    wydawnictwo=[]
    rodzaj=[]
    def czytaj(self, nr):
        return self.tytul[nr]
    def sortuj(self):
        self.tytul, self.autor, self.lstron, self.wydawnictwo, self.rodzaj = zip(*sorted(zip(self.tytul, self.autor, self.lstron, self.wydawnictwo, self.rodzaj)))
        return self.tytul, self.autor, self.lstron, self.wydawnictwo, self.rodzaj
        
    def strona(self, liczba):
        if liczba=="max":
            x=max(self.lstron)
            return "Maksymalna liczba stron to: " + x
        else:
            y=min(self.lstron)
            return "Minimalna liczba stron to: " + y
    

        
obiekt=Ksiazka()
p=input("Czy chcesz dodać książkę? Jeśli tak wpisz q")
while p=="q":
    x=input("Dodaj tytul: ")
    obiekt.tytul.append(x)
    y=input("Dodaj autor: ")
    obiekt.autor.append(y)
    z=input("Dodaj lstron: ")
    obiekt.lstron.append(z)
    c=input("Dodaj wydawnictwo: ")
    obiekt.wydawnictwo.append(c)
    h=input("Dodaj rodzaj: ")
    obiekt.rodzaj.append(h)
    p=input("Czy chcesz dodać książkę? Jeśli tak wpisz q")

    
print(obiekt.tytul)
print(obiekt.autor)
print(obiekt.lstron)
print(obiekt.wydawnictwo)
print(obiekt.rodzaj)
print(obiekt.czytaj(1))
print(obiekt.sortuj("rosnaco"))
print(obiekt.strona("min"))
'''
#3
'''
class Smartfon:
    listainst = []
    def __init__(self, marka, model, pamiec, procesor, kolor):
        self.marka = marka
        self.model = model
        self.pamiec = pamiec
        self.procesor = procesor
        self.kolor = kolor
        self.lista = [self.marka,self.model,self.pamiec,self.procesor,self.kolor]
        self.listainst.append(self)
    def iteracja(self,m):
        for m in lista:
            return self.model
        
    @staticmethod
    def wypisz():
        for instancja in Smartfon.listainst:
            print("marka = {}, model = {} , pamiec = {}, procesor = {}, kolor = {} ".format(instancja.marka, instancja.model, instancja.pamiec, instancja.procesor, instancja.kolor))
        
smart = Smartfon
smart1 = smart("Huiawei", "Modelowany", 100 , "Duzy", "Czarny")
smart2 = smart("Huiawei", "chujowy", 100 , "Duzy", "Czarny")
lista=[smart1,smart2]
print(smart1.iteracja("Huiawei"))
'''
#4
'''
class Student:
    listainst = []
    def __init__(self,imie,nazwisko,kierunek,srocen,checi):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kierunek = kierunek
        self.srocen = srocen
        self.checi = checi
        self.lista = [self.imie,self.nazwisko,self.kierunek,self.srocen,self.checi]
        self.listainst.append(self)
    def przedtsaw(self):
'''      

        
class Smartfon:
    listainst = []

    def __init__(self, marka, model, pamiec, procesor, kolor):
        self.marka = marka
        self.model = model
        self.pamiec = pamiec
        self.procesor = procesor
        self.kolor = kolor
        self.lista = [self.marka, self.model, self.pamiec, self.procesor, self.kolor]
        self.listainst.append(self)

    def modele_po_marce(self, marka):
        modele = []
        for instancja in self.listainst:
            if instancja.marka == marka:
                modele.append(instancja.model)
        if modele:
            print(f"Modele {marka}:")
            for model in modele:
                print(f"- {model}")
        else:
            print(f"Brak modeli dla marki {marka}")

smart = Smartfon("Huiawei", "Modelowany", 100, "Duzy", "Czarny")
smart1 = Smartfon("Huiawei", "chujowy", 100, "Duzy", "Czarny")
smart2 = Smartfon("Huiawei", "XD", 100, "Duzy", "Czarny")
smart3 = Smartfon("Samsung", "chujowy", 100, "Duzy", "Czarny")

smart.modele_po_marce("Samsung")
print(smart1.lista)