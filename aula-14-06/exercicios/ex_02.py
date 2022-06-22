# Busque qual são os anos da base de dados?

from Dados import load

header, data = load('compras.csv', [str, str, int, str, int, int, str])

anos = []

for line in data:
    if line['ano'] not in anos:
        anos.append(line['ano'])

print(anos)