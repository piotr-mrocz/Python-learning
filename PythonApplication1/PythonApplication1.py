#def multiArgs(*args): #spakuj wszystkie argumenty do args
#    suma = 0
#    for arg in args:
#        print(arg)
#        if (isinstance(arg,int) or isinstance(arg,float)): # isinstance(arg,int) - jeśli arg jest typu int
#            suma += arg
#    return suma


#nums = (1,2,3,4,5,6,7,8,'rabarbar')
#s = multiArgs(*nums) #rozpakuj na argumenty i wyślij fo funkcji 
#print ("suma",s)


f = lambda arg: arg + 1
print(f(3))

g = lambda a,b,c: (a+b)*c
print(g(2,3,4))

h = lambda arg: "dodatnia" if arg>0 else "niedodtnia"
print(h(2))
print(h(-2))


L = [1,2,3,4]
print(L)
newL = map(lambda x: x+1, L)
print(list(newL))

A = list(range(1,11))
print(A)

B = filter(lambda x: x%2==0, A)
print(list(B))


from functools import reduce

suma = reduce(lambda x,y: x+y, A)
print(suma)


def yieldPresentation():
    yield "a"
    yield 123
    yield 7

