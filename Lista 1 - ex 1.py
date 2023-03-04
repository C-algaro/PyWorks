i = 0
nota = []
acum = 0

while (i<4):
    var = float(input(f'Digite a nota {i+1}: '))
    nota.append(var)
    i+=1
    
i=0

print("\n\n------ Notas Digitadas: ------ ")
while (i<4):
    print(nota[i])
    acum = acum + nota[i]
    i+=1
    
print("\n\n------ Média das Notas ------ ")
print(acum/len(nota))
