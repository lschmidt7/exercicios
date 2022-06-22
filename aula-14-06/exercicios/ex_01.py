# Procure quem foi a pessoa que mais gastou?

from Dados import load

header, data = load('compras.csv', [str, str, int, str, int, int, str])

maior = {
    'compra': -1,
    'indice': 0
}

for idx, reg in enumerate(data):
    if reg['compra'] > maior['compra']:
        maior['compra'] = reg['compra']
        maior['indice'] = idx

pessoa = data[maior['indice']]

print(f'Maior compra: {pessoa["nome"]} {pessoa["sobrenome"]}')