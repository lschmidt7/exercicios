# Qual o valor gasto em compras por jovens do ano de 2010 até 2015?

from Dados import load

header, data = load('compras.csv', [str, str, int, str, int, int, str])

def faixa_etaria(reg):
    if 18 <= reg['idade'] <= 25:
        return 'jovem'
    elif 26 <= reg['idade'] <= 59:
        return 'adulto'
    elif reg['idade'] >= 60:
        return 'idoso'

valor_gasto = 0

for line in data:
    fe = faixa_etaria(line)
    if fe == 'jovem' and 2010 <= line['ano'] <= 2015:
        valor_gasto += line['compra']

print(f"Valor gasto: {valor_gasto}")