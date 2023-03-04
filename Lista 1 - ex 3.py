i = 0
lista_1 = []
lista_2 = []

while (i<10):
    var = int(input(f'Digite o valor {i+1} do vetor 1: '))
    lista_1.append (var)
    i+=1
print("\n\n")
i=0
while (i<10):
    var = int(input(f'Digite o valor {i+1} do vetor 2: '))
    lista_2.append (var)
    i+=1


print("\n\nLista 3:")
lista_3 = lista_1 + lista_2
print(sorted(lista_3))
