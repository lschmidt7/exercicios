# Exiba um gráfico que mostre a quantidade total de gastos com compras agrupadas por anos.

from matplotlib import pyplot

from Dados import load

header, data = load('compras.csv', [str, str, int, str, int, int, str])

gastos_por_ano = {}

for line in data:
    chave = line['ano']
    chave = str(chave)
    if chave not in gastos_por_ano:
        gastos_por_ano[chave] = 0
    gastos_por_ano[chave] += line['compra']

# sorted(gastos_por_ano.items())

anos = list(gastos_por_ano.keys())
anos.sort()

gastos = [gastos_por_ano[ano] for ano in anos]

fig, ax = pyplot.subplots()
ax.bar(anos, gastos)
pyplot.show()