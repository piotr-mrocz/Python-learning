#Zadanie3.
#Ania chce urządzić przyjęcie urodzinowe. Chce podzielić cukierki
#równo dla gości, a dla siebie zostawić resztę. Powiedz Justynie
#ile zostanie dla niej cukierków.
#Przykład:
#Podaj liczbę gości:
#10
#Podaj liczbę cukierków.
#32
#Dla Justyny zostaną 2 cukierki.

import math
goscie = int(input("Podaj liczbę gości: "))
cuksy = int(input("Podaj liczbę sukierków: "))
cuksyDlaGosci = (math.floor(cuksy/goscie)) * goscie;
print(f"Cuksy dla gości: {cuksyDlaGosci}")
cuksyDlaAni = cuksy - cuksyDlaGosci;
print(f"Dla Ani zostanie: {cuksyDlaAni}")
