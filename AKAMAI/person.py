def sumuj_liczby(a,b):
    suma = a + b
    wynik = str(suma)
    return print(wynik)

sumuj_liczby(2,3)

#-------------------------------------------------------------------------

class Pracownik:
    def __init__(self, imie, nazwisko, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon

    def przywitaj(self):
        print("Czesc, nazywam sie " + self.imie + " "+ self.nazwisko)

    def podajNumberTelefonu(self):
        print("{} to mój numer telefonu.".format(self.telefon))

