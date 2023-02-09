#LISTA
lista = ["iphone", "ipad", "notebook"]
lista.append("airpod")
print (lista)

#EXERCÍCIO - DICIONÁRIO
print ("\n")
precos = {
    'celular': 1500,
    'computador': 5000,
    'teblet': 2500,
}

for item in precos:
    print (precos [item])

#FORMATAÇÃO DE MOEDAS
print ("\n")
moeda = 1500
print (f'R${moeda:,.2f}')
    #O “F” antes do texto permite que você formate uma variável dentro dele, a variável fica entre chaves {}.
    # Dessa forma temos F’R${número}’ -> que vai se tornar R$1500.
    # Só que ainda faltaria formatar o separador de milhar que é a vírgula (,) em Python e as casas decimais (.00).
    # Para isso usamos a formatação dentro das chaves logo após o nome da variável.
    # Os ‘:’ (dois pontos) dizem que vamos fazer uma formatação.
    # A“,” (vírgula) diz que queremos o separador de milhar no número.
    # O “.2f” diz que queremos um “float” (número com casa decimal) com 2 casas decimais.

#TRATAMENTO E ANÁLISE DE DADOS
print ("\n")
with open('vendasLoja.txt', 'r') as arquivo:
    texto = arquivo.read()

lista_texto = texto.split("\n")
lista_texto = lista_texto [1:]
faturamento = 0

for linha in lista_texto:
    posicao_pv = linha.find(";") #Métodos de string
    valor = float(linha[posicao_pv+1 :])
    faturamento += valor

print (faturamento)