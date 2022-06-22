import csv
from random import randint

nomes = [
    'Miguel',
    'Arthur',
    'Gael',
    'Heitor',
    'Theo',
    'Davi',
    'Gabriel',
    'Bernardo',
    'Samuel',
    'Helena',
    'Alice',
    'Laura',
    'Valentina',
    'Heloisa',
    'Maria',
    'Sophia'
]

sobrenomes = [
    'Santos',
    'Maia',
    'Silva',
    'Soares',
    'Oliveira',
    'Souza',
    'Rodrigues',
    'Ferreira',
    'Alves',
    'Pereira',
    'Alves',
    'Gomes',
    'Martins',
    'Ribeiro'
]

idades = {'min': 18, 'max': 70}

compras = {'min': 500, 'max': 10000}

anos = {'min': 2005, 'max': 2020}

pagamentos = ['dinheiro', 'debito', 'credito']

registros = 5000

f = open('compras.csv', mode='w', newline='')
writer = csv.writer(f, delimiter=',', quotechar='"')

writer.writerow(['nome','sobrenome','idade','sexo','compra','ano','pagamento'])

for r in range(registros):
    index_nome = randint(0, len(nomes) - 1)
    index_sobrenome = randint(0, len(sobrenomes) - 1)
    index_pagamento = randint(0,2)
    
    nome = nomes[index_nome]
    sobrenome = sobrenomes[index_sobrenome]
    
    idade = randint(idades['min'], idades['max'])
    compra = randint(compras['min'], compras['max'])
    ano = randint(anos['min'], anos['max'])
    pagamento = pagamentos[index_pagamento]

    sexo = 'M' if index_nome < 9 else 'F'

    row = [nome, sobrenome, idade, sexo, compra, ano, pagamento]

    writer.writerow(row)

f.close()