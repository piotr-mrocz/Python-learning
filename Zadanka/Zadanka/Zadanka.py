# Napisz metodę, która zwróci Twój aktualny wiek.

def wiek():
    moj_wiek = 22
    return (moj_wiek)
print(wiek())


# Napisz metodę, która zwróci Twoje imię,

def imie():
    imie = "co cię to, kurna, obchodzi"
    return imie
print(imie())


# Napisz metodę, która jako argument przyjmuje 2 liczby i wypisuje ich sumę, różnicę i iloczyn

def dzialania(a,b=0,c=0):
    suma = a+b+c
    roznica = a-b-c
    iloczyn = a*b*c
    return ("Suma: ",suma," różnica: ",roznica," iloczyn: ",iloczyn)
print(dzialania(1,2,3))

# Napisz metodę, która jako argument przyjmuje liczbę i zwraca true jeśli liczba jest parzysta

def czyParzysta(a):
    return  "parzysta" if a%2==0 else "nieparzysta"
print(czyParzysta(7))
print(czyParzysta(4))

# Napisz metodę, która jako argument przyjmuje liczbę 
# i zwraca true jeśli liczba jest podzielna przez 3 i przez 5,

def podzielna(a):
    return "true" if a%15==0 else "false"
print(podzielna(10))
print(podzielna(60))


# Napisz metodę, która jako argument przyjmuje liczbę i zwraca go podniesionego do 3 potęgi

def potega(a):
    return a*a*a
print(potega(2))


# Napisz metodę, która jako argument przyjmuje liczbę i zwraca jej pierwiastek kwadratowy 

import math as m

def pierwiastek_kwadratowy(a):
    return m.sqrt(a)
print(pierwiastek_kwadratowy(9))

