# Utilizando as faixas etárias, diga quantas pessoas há em cada faixa?

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

faixa = {
    'jovem': 0,
    'adulto': 0,
    'idoso': 0
}

for line in data:
    chave = faixa_etaria(line)
    faixa[chave] += 1

print(faixa)