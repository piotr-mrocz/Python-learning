#  Napisać program, który pobiera od użytkownika liczbę całkowitą dodatnią,
#  a następnie wyświetla na ekranie kolejno wszystkie liczby niepatrzyste
#  nie większe od podanej liczby.  Przykład, dla 15 program powinien wyświetlić
#  1, 3, 5, 7, 9, 11, 13, 15.
x = int(input("Ino dej liczbę: "))
suma = 0
for i in range(1, x + 1):
    if i % 2 != 0:
        suma += 1
        print(i)
print()
print("Łącznie: ",suma)
