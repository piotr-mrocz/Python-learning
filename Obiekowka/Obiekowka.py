class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def PrzedstawSie(self):
        print("Nazywam się {} {}.".format(self.imie, self.nazwisko))


Jan = Osoba("Jan", "Kowalski")
Jan.PrzedstawSie()

class Ktos:
    def __init__(self, imie, nazwisko):
        self._imie = imie
        self.__nazwisko = nazwisko

    def PrzedstawSie(self):
        print("Nazywam się {} {}.".format(self._imie, self.__nazwisko))


Adam = Ktos("Adam", "Adamski")
Adam.PrzedstawSie()


class Test:
    def __init__(self):
        self.publiczne, self._chronione, self.__prywatne = 1, 2, 3
def main():
    test = Test()
    print(test.publiczne)
    print(test._chronione)
    print(test._Test__prywatne)
if __name__ == "__main__":
    main()