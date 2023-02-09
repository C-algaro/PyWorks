print('Bem-vindo ao sistema do INSS \n')

nome = input('Digite o seu nome: ')
idade = int(input('Insira a sua idade: '))

ano = 2023-idade+65
print ('\nVocê se aposentará no ano de:', ano)

if idade <= 65:
    print ('Daqui', 65-idade, 'anos \n')

else:
    print ('Você já pode se aposentar \n')