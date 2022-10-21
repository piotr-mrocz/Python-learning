def Pobierz_dane():
    marka = input("Podaj markę: ")
    model = input("Podaj model: ")
    pojemnosc = int(input("Podaj pojemność: "))
    max_predkosc = int(input("Podaj maksymalną prędkość: "))
   
    auta = {
        'Marka': marka,
        'Model': model,
        'Pojemnosc': pojemnosc,
        'Max_predkosc': max_predkosc
        }
    return auta


def Wyswietl(auta):
    for keys,values in auta.items():
        print(keys,":",values)


a = Pobierz_dane()
Wyswietl(a)








# TEŻ ZADZIAŁA
#def wprowadzDane():

#    dict = {​​
#        'Marka':input("Podaj marke: "),
#        'Model':input("Podaj model: "),
#        'Pojemosc':input("Podaj pojemnosc: "),
#        'Predkoscmax':input("Podaj prekdoscmax: ")
#    }​​

#    return dict



#def wyswietl(dict):
#    print("\n")
#    for keys,values in dict.items():
#        print(keys,":",values)

#a = wprowadzDane()

#wyswietl(a)