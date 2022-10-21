import math

imie1 = input("Podaj swoje imię: ")
nazwisko1 = input("Podaj swoje nazwisko: ")
wiek1 = int(input("Podaj swój wiek: "))
print()

imie2 = input("Podaj swoje imię: ")
nazwisko2 = input("Podaj swoje nazwisko: ")
wiek2 = int(input("Podaj swój wiek: "))
print()

print("User1: imię i nazwisko, wiek: {0} {1}, {2}".format(imie1, nazwisko1, wiek1))
print("User2: imię i nazwisko, wiek: {0} {1}, {2}".format(imie2, nazwisko2, wiek2))
sr_wiek = round((wiek1 + wiek2)/2, 2)
print("Średni wiek: {0}".format(sr_wiek))

surname = "Kowalski"
print(surname[0]) # K
print(surname[0 : 3]) # Kow
print(surname[-2]) # k
print(surname[-2:]) # ki
print(surname[: -2]) # Kowals
print(surname[: -2 : 2]) # Kwl co drugi znak
