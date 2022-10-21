#  Utwórz klasę Human reprezentującą człowieka, musi posiadać atrybuty takie jak 
#  wiek, waga, wzrost, imię i płeć. Klasa powinna także zawierać metody
#   getAge, getWeight, getHeight, getName, isMale

class Human:
    def getAge(self):
        return
    def getWeight(self):
        return
    def getHeight(self):
        return
    def getName(self):
        return
    def isMale(self):
        return



# Utwórz klasę reprezentującą prostokąt, musi posiadać 
# atrybuty długość i szerokość. Klasa powinna posiadać 
# metody obliczające pole(area), obwód(circuit) 
# i długość przekątnej(diagonal length).
import math
class Rectangle():
    def Circuit(self, a,b):
        return a+a+b+b

    def Area(self, a,b):
        return a*b

    def DiagonalLength(self,a,b):
        c = math.sqrt((a*a)+(b*b))
        return c

rectangle = Rectangle()
print("Pole: ", rectangle.Area(3,4))
print("Obwód: ", rectangle.Circuit(3,4))
print("Długość przekątnej: ", rectangle.DiagonalLength(3,4))


