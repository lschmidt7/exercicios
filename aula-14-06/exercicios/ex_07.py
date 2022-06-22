# Qual é a faixa etária que mais gasta?

# Jovens, 18 a 25 anos
# Adultos, 26 a 59 anos
# Idosos, igual ou maior que 60 anos

from Dados import load

header, data = load('compras.csv', [str, str, int, str, int, int, str])

def faixa_etaria(reg):
    if 18 <= reg['idade'] <= 25:
        return 'jovem'
    elif 26 <= reg['idade'] <= 59:
        return 'adulto'
    elif reg['idade'] >= 60:
        return 'idoso'

def maior(gastos):
    maior_gasto = 0
    maior_gasto_faixa_etaria = ''
    for gasto in gastos.items():
        if gasto[1] > maior_gasto:
            maior_gasto = gasto[1]
            maior_gasto_faixa_etaria = gasto[0]
    return maior_gasto_faixa_etaria


gastos_faixa_etaria = {
    'jovem': 0,
    'adulto': 0,
    'idoso': 0
}

for line in data:
    chave = faixa_etaria(line)
    gastos_faixa_etaria[chave] += line['compra']

print(maior(gastos_faixa_etaria))
