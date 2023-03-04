notas = []
acima = []
abaixo = []
i = 0

while (notas != -1):
    var = float(input(f'Informe o valor da nota {i+1}: '))
    if var == -1:
        break;
    notas.append (var)
    i+=1
i=0

print("\n")
print(f'* Quantidade de valores que foram lidos: {len(notas)}')
print(f'* Valores na ordem que foram informados : {notas}')
print(f'* Valores na ordem ordenados : {sorted(notas)}')
print(f'* Soma dos valores : {sum(notas)}')
print(f'* Média dos valores : {sum(notas)/len(notas)}')
while (len(notas) > i):
    if notas[i] > sum(notas)/len(notas):
        acima.append (notas[i])
    elif notas[i] < sum(notas)/len(notas):
        abaixo.append (notas[i])
    i+=1
print(f'* Quantidade de valores acima da média : {acima}')
print(f'* Quantidade de valores abaixo da média : {abaixo}')
print("  Programa finalizado")
