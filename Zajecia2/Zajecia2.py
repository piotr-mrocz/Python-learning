x = int(input("Podaj 1 wartość: "))
y = int(input("Podaj 2 wartość: "))
z = int(input("Podaj 3 wartość: "))




if x > y and x > z:
    print(f"Największa wartość to wartość 1 i wynosi: {x}")
elif y > z:
    print(f"Największa wartość to wartość 2 i wynosi: {y}")
else:
     print(f"Największa wartość to wartość 3 i wynosi: {z}")