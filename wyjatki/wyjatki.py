boolean = 1
while boolean < 5:
    try:
        a = int(input("Pierwsza liczba: "))
        b = int(input("Druga liczba: "))
        print(a/b)
    except ZeroDivisionError:
        print("Nie dzieli się przez 0")
    except ValueError:
        print("Niepoprawna wartość!")
    finally:
        print("Skończmy to w końcu")
        boolean += 1