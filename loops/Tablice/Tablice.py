# Utwórz metodę pobierającą dodatnią liczbę całkowitą X, która wyświetli na ekranie liczby od zera do X
def loop(x):
    for i in range (1, x+1):
        print(i)
    return i

x = int(input("Ino dej liczbę: "))
loop(x)

