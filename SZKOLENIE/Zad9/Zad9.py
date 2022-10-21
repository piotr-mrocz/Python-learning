#Zadanie9.
#Odczytaj wiek danej osoby i sprawdź czy osoba jest nastolatkiem.
#Zakładamy, że osoba jest nastolatkiem jeśli ma od 13
#do 17 lat.

wiek = int(input("Podaj swój wiek: "))

if wiek <= 17 and wiek >= 13:
    print("Jesteś nastolatkiem")
else:
    print("Nie jesteś nastolatkiem")