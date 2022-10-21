#Zadanie10.
#Michał pije kawę o godzinie 9 i 12.
#Napisz program, który pokazuje czy Michał ma wypić
#kawę.


import datetime

obecnaGodzina = datetime.datetime.now().hour
obecnaMinuta = datetime.datetime.now().minute
obecnaSekunda = datetime.datetime.now().second
print(f"Aktualna godzina {obecnaGodzina} : {obecnaMinuta} : {obecnaSekunda}")


if obecnaGodzina == 9 or obecnaGodzina == 12 and obecnaMinuta == 0 and obecnaSekunda == 0:
    print("Michał, wypij kawę!")
else:
    print("Michał, to nie pora na kawę!")