# Qual foi o gasto por ano?
from Dados import load

header, data = load('compras.csv', [str, str, int, str, int, int, str])

anos = {}

for line in data:
    chave = line['ano']
    if chave not in anos:
        anos[chave] = 0
    anos[chave] += line['compra']

print(anos)