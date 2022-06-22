# Qual foi o ano com maior gasto?

from Dados import load

header, data = load('compras.csv', [str, str, int, str, int, int, str])

anos = {}

for line in data:
    chave = line['ano']
    if chave not in anos:
        anos[chave] = 0
    anos[chave] += line['compra']

maior_gasto = 0
maior_gasto_ano = 0

for ano in anos.items():
    if ano[1] > maior_gasto:
        maior_gasto = ano[1]
        maior_gasto_ano = ano[0]

print(maior_gasto_ano)