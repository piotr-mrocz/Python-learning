worker = {
    'name' : 'Jan',
    'surname' : 'Kowalski',
    'city' : 'Poznań',
    'age' : 20
    }


countOfChildren = int(input("Ilość dzieci: "))
listChildren = []

for x in range (countOfChildren):
    nameChildren = input("Podaj imię dziecka: ")
    listChildren.append(nameChildren)

workerChildren = {'childrenNames' : str(listChildren)}
worker.update(workerChildren)

mother = input("Podaj imię matki: ")
father = input("Podaj imię ojca: ")
parentNames = {'parentnames' : str([mother, father])}
worker.update(parentNames)
print(worker)
print()

for key, value in worker.items():
    print (f'{key} : {value}')