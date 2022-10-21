#Zadanie16.
#Odczytaj 2 liczby i wypisz na ekran największą z liczb.

liczba1 = int(input("Podaj 1 liczbę: "))
liczba2 = int(input("Podaj 2 liczbę: "))


if liczba1 > liczba2:
    print(f"Największa liczba to: {liczba1}")
elif liczba1 == liczba2:
    print("Obie liczby są równe")
else:
    print(f"Największa liczba to: {liczba2}")
