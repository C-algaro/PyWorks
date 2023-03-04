from random import randint

i = 0
lista_1 = []
lista_2 = []

while (i<10):
    var = randint(1,99)
    lista_1.append (var)
    i+=1
i=0
while (i<10):
    var = randint(1,99)
    lista_2.append (var)
    i+=1


lista_3 = lista_1 + lista_2
print(sorted(lista_3))
