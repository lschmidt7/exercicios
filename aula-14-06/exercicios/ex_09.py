# Qual o sobrenome que mais aparece na base de dados?

from re import S
from Dados import load

header, data = load('./compras.csv', [str, str, int, str, int, int, str])

sobrenomes = {}

for line in data:
    s = line['sobrenome']
    if s not in sobrenomes:
        sobrenomes[s] = 0
    sobrenomes[s] += 1

sobrenome_mais_comum = {
    'ocorrencias': 0,
    'sobrenome': ''
}

for sobrenome in sobrenomes.items():
    if sobrenome[1] > sobrenome_mais_comum['ocorrencias']:
        sobrenome_mais_comum['ocorrencias'] = sobrenome[1]
        sobrenome_mais_comum['sobrenome'] = sobrenome[0]

print(f'Sobrenome mais comum: {sobrenome_mais_comum["sobrenome"]}')