import os
file = open("dane.txt", "w", encoding= "utf-8")

file.write("Gdy Cię nie widzę\n")
file.write("Nie wzdycham, nie płaczę\n")
file.write("Nie tracę zmysłów\n")
file.write("Kiedy Cię zobaczę\n")
file.write("Jednakże, gdy Cię długo nie oglądam\n")
file.write("Czegoś mi braknie, kogoś widzieć żądam\n")
file.write("I tęskniąc sobie powtarzam pytanie:\n")
file.write("Czy to jest przyjaźń, czy to jest kochanie?\n")
file.close()



# czytanie linii:

if os.path.exists("dane.txt"):
    file = open("dane.txt", "r", encoding = "utf-8")
    file_total = file.read()  # czyta wszystko do jednej zmiennej   ----> jeden wielki napis
    print(file_total)
    file.close()



if os.path.isfile("dane.txt"):
    file = open("dane.txt", "r", encoding = "utf-8")
    file.seek(0)
    lines = file.readlines()    # czyta każdą linię osobno   ------> zwraca listę zczytanych liń
    print(lines)
    file.close()

print()
print()
# os.remove("dane.txt")    usuwa plik
# os.rename("dane.txt", "plik.txt")      zmiana nazwy


# otworzenie pliku z konstrukcją WITH
# konstrukcja ta automatycznie zamknie za nas plik

# with open("dane.txt", "r", encoding = "utf-8") as zmienna:



#  PIKLOWANIE  - zapisywanie i wczytywanie obiektów do/z plików w sposób binarny

import pickle

# zapis obiektów do pliku (binarnie)
lista = [10,20,"trzydzieści",[1,2,"trzy"]]
with open("dane.pickle", "wb") as outPut:
    pickle.dump(lista, outPut)
    outPut.close()


# odczyt obiektów binarnych z plików
with open("dane.pickle","rb") as inPut:
    unpickle = pickle.load(inPut)
print(unpickle, type(unpickle))