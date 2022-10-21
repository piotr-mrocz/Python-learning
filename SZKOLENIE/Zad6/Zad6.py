#Zadanie6.
#Odczytaj liczbę i wypisz na ekran 10*liczba. Uwzględnij
#niepoprawne dane.

#Przykład dla danych
#20
#Wynik:
#200
#Dla danych
#Aaa
#Wynik:

#To nie jest poprawna liczba

try:
    liczba = int(input("Podaj liczbę: "))
    print(liczba * 10)
except :
    print("Niestety podałeś niepoprawne dane!")

