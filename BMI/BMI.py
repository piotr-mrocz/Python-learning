# Napisać program, który oblicza wartość współczynnika BMI (ang. body mass index) 
# wg. wzoru: waga/wzrost^2 . Jeżeli wynik jest w przedziale (18,5 - 24,9) 
# to wypisuje ”waga prawidłowa”, jeżeli poniżej to ”niedowaga”, jeżeli powyżej ”nadwaga”.

waga = float(input("Waga w kg: "))
wzrost = float(input("Wzrost w m: "))

BMI = waga/(wzrost*wzrost)

print(BMI)

if BMI > 24.9:
    print("Nadwaga")

elif BMI < 18.5:
    print("Niedowaga")

else:
    print("Waga prawidłowa")