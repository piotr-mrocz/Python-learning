import math

class Funkcja_Kwadratowa():
    def Delta(self, a, b, c):
        delta = ((b*b) - 4 * a * c)
        return delta

    def MiejsceZerowe1(self):
        x1 = ((-b - (math.sqrt(delta)))/(2 * a))
        return x1

    def MiejsceZerowe2(self):
        x2 = ((-b + (math.sqrt(delta)))/(2 * a))
        return x2



funkcja_kwadratowa = Funkcja_Kwadratowa()

print("Delta wynosi: {}".format(funkcja_kwadratowa.Delta(2, 3, (-2))))
print("Miejsca zerowe: {} i {}".format(funkcja_kwadratowa.MiejsceZerowe1, 
                                       funkcja_kwadratowa.MiejsceZerowe2 ))

miejsce_zerowe = funkcja_kwadratowa.MiejsceZerowe1(x1)
print(miejsce_zerowe)