par = []
impar = []
i = 0

while (i < 20):
    var = int(input(f'Digite o valor {i+1}: '))
    if var%2==0:
        par.append(var)
    else:
        impar.append(var)
    i+=1

    
print("\n\n")
lista = par + impar
print(f'Vetor Lista: {sorted(lista)}')
print(f'Vetor Par: {sorted(par)}')
print(f'Vetor Impar: {sorted(impar)}')
