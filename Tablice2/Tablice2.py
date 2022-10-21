# Napisać program, który:
#• utworzy tablicę 10 liczb całkowitych i wypełni 
# ją wartościami losowymi zprzedziału 
# [−10, . . . , 10],
#• wypisze na ekranie zawartość tablicy,
#• wyznaczy najmniejszy oraz najwięszy element 
#w tablicy,
#• wyznaczy średnią arytmetyczną elementów tablicy,
#• wyznaczy ile elementów jest mniejszych, 
#ile większych od średniej.

import random as r
import math as m

# uzupełnienie listy losowymi liczbami
lista = []
for i in range (1, 11):
    lista.append(r.randint(-10, 10))

# wyświetlenie listy, max i min liczby
print(lista)
print("Największa liczba: ", max(lista))
print("Najmniejsza liczba: ", min(lista))
print()

# obliczanie średniej arytmetycznej
suma = 0
for j in lista:
    suma += j
srednia = suma/10
print("Średnia arytmetyczna: ",srednia)

# obliczanie ilości liczb poniżej i powyżej średniej

ponizej = 0
powyzej = 0

for a in lista:
    if a > srednia:
        powyzej += 1
    elif a < srednia:
        ponizej += 1

print("Ilość liczb mniejszych od średniej: ",ponizej)
print("Ilość liczb większych od średniej: ",powyzej)
print()
