#Funkcja kwadratowa
#Napisz klasę FunkcjaKwadratowa, która przechowuje funkcje typu 
#$ax^2$+bx+c. Klasa powinna zawierać trzy pola: a, b, c, 
#które są przypisywane w konstruktorze. Główną metodą powinna być 
#Rozwiaz(), która zwraca miejsca zerowe podanej funkcji. 
#Należy zwrócić uwagę na przypadki gdy a=0, b=0 lub c=0, 
#a także obmyślić sposób informowania o nieskończonej liczbie, 
#jednym lub zerze rozwiązań.

class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Rozwiaz(self):
        delta = ((b*b) - (4*a*c))
        print("Delta wynosi: ", delta)

        pierwiastek_z_delty = sqrt(delta)
        print("Pierwiastek z delty wynosi: ", pierwiastek_z_delty)

        X1 = (((-b) - pierwiastek_z_delty) / (2*a))
        print("Pierwsze miejsce zerowe wynosi: ", X1)

        X2 = (((-b) + pierwiastek_z_delty) / (2*a))
        print("Drugie miejsce zerowe wynosi: ", X2)

        return X1, X2

def main():
    funkcja = FunkcjaKwadratowa(3, 2, (-2))
    print(funkcja.Rozwiaz())


if __name__ == "__main__":
    main()




