#Zadanie5.
#Odczytaj liczbę i pokaż na ekran liczbę cyfr danej liczby.
#Przykład:
#Podaj liczbę
#200
#Liczba ma 3 cyfry.

liczba = int(input("Podaj liczbę: "))
iloscCyfr = 0
for x in str(liczba):
    iloscCyfr += 1

print(f"Liczba ma {iloscCyfr} cyfry")