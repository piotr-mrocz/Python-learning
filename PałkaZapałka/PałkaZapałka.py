# taki znaczek oznacza komentarz, nie wpływa na działanie kodu, ale czasem się przydaje 
# tym bardziej, że tutaj ma to zielony kolor, więc wygląda to prawie jak w matrixie :D 

print("Hello world!") # print = wydrukuj, czyli wypisz coś na ekranie. 
                      # W naszym przypadku będzie to napis Hello world!
                      # Napisy zawsze zapisuje się w cudzysłowie "No jakiś tam napis"

napis = "Jakaś tam wartość"  # napis to nasza zmienna
                             # zmienna to taka szufladka, która będzie przetrzymywać jakąś wartość
print(napis)                 # no i znowu print = wypisz na ekranie naszą zmienną napis

delfin = input("Wpisz coś: ")  # żeby pobrać jakąś wartość z klawiatury użyjemy słówka input
                               # to co mamy w nawiasie wyświetli się zanim pobierzemy dane od użytkownika
                               # automatycznie zostanie to zapisane w naszej zmiennej o nazwie delfin :) 
print(delfin)                  # no i znowu print = wypisz na ekranie to, co przechowuje zmienna delfin

# Wszystko fajnie, pięknie, ale... Wszystko, co jest wczytywane jest klasy string (nie chodzi o galoty)
# string w programowaniu to napis, ale co zrobić, gdy chcemy wczytać liczbę? Ano trzeba o tym poinformować kompa
liczba = int(input("Dej no liczbę: ")) # ten jakże piękny wyraz int oznacza właśnie, że chcemy wczytać liczbę
                                       # i to liczbę całkowitą, czyli bez przecinka
                                       # float natomiast to liczby z przecinkami
                                       # więc to, co wczytamy teraz już będzie liczbą i możemy robić 
                                       # różne arytmetyczne pierdolamento
                                       # ta liczba zostanie zapisana w naszej zmiennej liczba
print(liczba)                          # no i nie chce być inaczej... print = wypisz na ekranie to, co 
                                       # przechowuje nasza zmienna liczba