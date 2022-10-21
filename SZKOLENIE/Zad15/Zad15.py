#Zadanie15.
#Zagadka napisz program, który każe o zgadniecie jakie liczby
#należy wstawić pod znak zapytania:
#1 3 5 ? 9
#2 4 6 ? 10

end = False
while end != True:
    print("1 3 5 ? 9")
    print("2 4 6 ? 10")
    print("Podaj liczby, które kryją się pod ?")
    pierwszy = int(input("co kryje się pod pierwszym ? : "))
    drugi = int(input("co kryje się pod drugim ? : "))

    if pierwszy == 7 and drugi == 8:
        print("Udało się!")
        end = True
    else:
        print("Spróbuj jeszcze raz!")

