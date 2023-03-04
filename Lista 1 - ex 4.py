nome = 0
contador = 0
suspeita = []
cumplice = []
assassino = []
inocente = []

print ("\n-----------------------------------------------")
print("Responda às perguntas com:")
print("Sim ou Não \n")
print("Digite 'Sair' para terminar as interrogações")
print("----------------------------------------------- \n")


while (nome != 'Sair'):
    nome = input("Nome da pessoa interrogada: ")

    if nome == 'sair' or nome == 'Sair' or nome == 'SAIR':
        break;

    #Questionário:
    print("")
    print("Telefonou para a vítima?")
    resposta = input("Resposta: ")
    if resposta == 'sim' or resposta == 'Sim' or resposta == 'SIM':
      contador+=1
      
    print("Esteve no local do crime?")
    resposta = input("Resposta: ")
    if resposta == 'sim' or resposta == 'Sim' or resposta == 'SIM':
      contador+=1

    print("Mora perto da vítima?")
    resposta = input("Resposta: ")
    if resposta == 'sim' or resposta == 'Sim' or resposta == 'SIM':
      contador+=1

    print("Devia para a vítima?")
    resposta = input("Resposta: ")
    if resposta == 'sim' or resposta == 'Sim' or resposta == 'SIM':
      contador+=1

    print("Já trabalhou com a vítima?")
    resposta = input("Resposta: ")
    if resposta == 'sim' or resposta == 'Sim' or resposta == 'SIM':
      contador+=1

    print("")


    #Classificação do Interrogado:
    if contador == 2:
      suspeita.append (nome)

    elif contador == 3 or contador == 4:
      cumplice.append (nome)

    elif contador == 5:
      assassino.append (nome)

    else:
      inocente.append (nome)

    #Resultado:
print("\n\nResultado:")
print(f'*Inocentes: {inocente}')
print(f'*Suspeitos: {suspeita}')
print(f'*Cúmplices: {cumplice}')
print(f'*Assassino: {assassino}')
