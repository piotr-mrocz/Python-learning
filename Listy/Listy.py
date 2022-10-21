#Dodaj listę o nazwie: country
#Przypisz do niej 5 elementów
#Poproś użytkownika, aby dodał dwa nowe elementy do listy
#Uzytkownikowi wyświetl listę do wyboru:

#1) Wyświetl pierwsze 3 elementy listy
#2) Wyświetl elementy listy, które dodałem (dane pobierz z listy)
#3) Wyświetl zawartość listy
#4) Wyczyść zawartość listy
#5) Znajdź element w liście, który poda użytkownik (wyświetl czy jest dodany do listy)

#Użytkownik raz dokonuje wyboru z listy.
#Wyświetl zawartość listy po wykonaniu operacji przez użytkownika

country = ["Polska", "Niemcy", "Czechy", "Argentyna", "Brazylia"]

country1 = input("Podaj państwo: ")
country.append(country1)
country2 = input("Podaj drugie państwo: ")
country.append(country2)


print("Pierwsze 3 elementy z listy country: " + str(country[0:3]))
print("Elementy dodane przez użytkownika: " + str(country[-2]) + " i " + str(country[-1]))
print("Cała zawartość listy: " + str(country))

country.clear()
print("Cała zawartość listy: " + str(country))
