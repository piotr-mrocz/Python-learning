#1) Użytkownik podaje z klawiatury dane: imie, nazwisko, telefon
#2) Zakładając, że użytkownik podaje polskie imię spradź czy jest kobietą czy mężczyzną 
#(sprawdź po podanym imieniu)
#3) Użytkonicy nie zawsze podają imiona i nazwiska z dużej litery (popraw dane podane przez 
#   użytkownika)
#4) Spradź czy imię i nazwisko zawiera tylko litery
#   numer telefonu zawwiera tlyko cyfry
#5) Wyczyść podany numer telefonu z myślników i spacji np. 111-222-333 =>    1112223333
#6) Przypisz do zmiennej dane: policz ile mają liter a ile cyfr i wypisz na ekranie w formacie: 
#  Ilość liter w zmiennej ... wynosi: ...
#  Ilość cyfr w zmiennej ... wynosi: ...

name = input("Podaj imię: ")
name = name.title()
surname = input("Podaj nazwisko: ")
surname = surname.title()
phone = input("Podaj numer telefony: ")
phone = phone
sex = ""

# SPRAWDZANIE PŁCI
if name.lower().endswith("a") == True:
    sex = "Kobieta"
else:
    sex = "Mężczyzna"

print(name, surname, sex, phone)

# SPRAWDZANIE POPRAWNOŚCI WPROWADZONYCH DANYCH
if name.isalpha() == True or surname.isalpha() == True:
    print("Imię i nazwisko składa się z samych iter")
else:
    print("Niepoprawne dane! Imię i nazwisko musi składać się z samych liter!")

if phone.isdigit() == True:
    print("Numer telefonu składa się z samych cyfr")
else:
    print("Niepoprawne dane! Numer telefonu musi składać się z samych cyfr!")

