# PROCEDURY

def UmyjRece():
    print("Łapy")


def Mniam(produkt):
    print("jem " + produkt)

def JedzObiad(produkty):
    for x in produkty:
        print("Jem ",x)


ProduktyNaObiad = ["kotlety", "kartofle", "brokuły"]

UmyjRece()
Mniam(input())
JedzObiad(ProduktyNaObiad)