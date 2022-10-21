# Napisz program, który pobierze od użytkownika liczbę całkowitą N 
# reprezentującą długość tablicy, a następnie poprosi o N kolejnych 
# liczb uzupełniając nimi wcześniej stworzoną tablicę. Wyświetl na konsoli 
# tablicę posortowaną w kolejności od najmniejszej do największej liczby

a = int(input("Dej no liczbę: "))

lista = []

for i in range (1, a + 1):
    b = float(input("Dej no liczbę: "))
    lista.append(b)

for j in sorted(lista):
    print(j)