import time
import os
import sys


baza_danych = {
               "bułka pszenna" : 200, 
               "plaster zielonego ogórka": 3, 
               "marchewka" : 15, 
               "leczo" : 185, 
               "kromka chleba żytniego" : 79, 
                "łyżka masła" : 75, 
                "guliver karmel" : 256, 
                "kitkat biały" : 207, 
                "plaster szynki mielonki" : 35
                }


while (True):
    print()
    print("*** ZROBIMY WSZYSTKO, ŻEBYŚ NIE BYŁ GRUBSZY NIŻ JESTEŚ ***")
    print("*                                                        *")
    print("*      1. Wprowadź dzienny limit kaloryczny              *")
    print("*      2. Sprawdź naszą bazę danych                      *")
    print("*      3. Wprowadź listę spożytych kalorii               *")
    print("*      4. Wyjdź                                          *")
    print("*                                                        *")
    print("**********************************************************")
    
    choice = input("Wybierz opcję: ")

    if (choice == "1"):
        limit = float(input("Podaj dzienny limit kaloryczny: "))
        print(limit)
        time.sleep(0.7)
        os.system('cls||clear')


    elif (choice == "2"):
        print("Oto nasza baza danych:")
        for wers in baza_danych:
            print ("{wers}: {wartosc}".format(wers = wers, wartosc = baza_danych[wers]))

        input("Wyśnij jakiś klawisz, by wrócić do menu...")
        time.sleep(0.7)
        os.system('cls||clear')

        
    elif (choice == "3"):
        suma = 0

        while(True):

            produkt = input("Podaj produkt: ")
            if(produkt != "koniec"):
                wartosc = baza_danych[produkt]
                print("Wartość kaloryczna podanego produktu wynosi: {wartosc}".format(wartosc = wartosc))
                suma = (suma + wartosc)
                print("Suma spożytych kalorii wynosi: {suma}".format(suma = suma))

            else:
                os.system('cls||clear')
                print("Suma spożytych kalorii wynosi: {suma}".format(suma = suma))

                if(suma > limit):
                    print("Jeszcze trochę i będziesz ważyć tyle co stado słoni... Weź się za siebie..")
                    time.sleep(0.5)
                    input("Wyśnij jakiś klawisz, by wrócić do menu...")

                else:
                    print("Oby tak dalej... Jesteś coraz bliżej sukcesu...")
                    time.sleep(0.5)
                    input("Wyśnij jakiś klawisz, by wrócić do menu...")
                break



    elif (choice == "4"):
        odp = input("Czy na pewno chcesz wyjść? T/N: ")

        if (odp == "T" or odp == "t"):
            print("To pa")
            break
            
        else:
            time.sleep(0.7)
            os.system('cls||clear')
    
    
    else:
        print("Coś poszło nie tak... \nSpróbuj jeszcze raz")
        time.sleep(0.9)
        os.system('cls||clear')
        
    
