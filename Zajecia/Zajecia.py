#list = ['name', 'surname', 'age', 'end', 'city']


#for x in list:
#    if x=='end':
#        print("Koniec pętli")
#        break
#    print(x)

import math
liczba1 = int(input("Pierwsza liczba: "))
liczba2 = int(input("Druga liczba: "))

start = max(liczba1, liczba2)
end = min(liczba1, liczba2)

for x in range(start, end, -1):
    print(x)
