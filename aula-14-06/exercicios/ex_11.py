# Qual opção de pagamento é mais utilizada em cada faixa etária?

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
    'jovem': {
        'debito': 0,
        'credito': 0,
        'dinheiro': 0
    },
    'adulto': {
        'debito': 0,
        'credito': 0,
        'dinheiro': 0
    },
    'idoso': {
        'debito': 0,
        'credito': 0,
        'dinheiro': 0
    }
}

for line in data:
    fe = faixa_etaria(line)
    pg = line['pagamento']
    faixa[fe][pg] += 1

print(faixa)
