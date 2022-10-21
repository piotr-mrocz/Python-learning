#Zadanie12.
#Odczytaj wyraz i wypisz na ekran wartość True lub False w
#zależności od tego czy wyraz zawiera w sobie napis kot


wyraz = input("Poproszę o wyraz: ")

if wyraz.count("kot") <= 0:
    print("False")
else:
    print("True")