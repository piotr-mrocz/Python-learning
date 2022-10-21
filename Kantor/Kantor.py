# napisz funkcję, która przyjmuje jako argument ilość złotych jakie posiada klient
# zwróc info ile franków może otrzymać

pln = float(input("Proszę podać kwotę: "))
kursChf = 4.2492

def plnToChf(pln):
    wymienionePln = round(pln/kursChf, 2)
    print(f"Za podaną kwotę można otrzymać {wymienionePln} franków szwajcarskich")

plnToChf(pln)