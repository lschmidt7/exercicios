# Qual foi o ano em que os homens mais usaram o crédito?

from Dados import load

header, data = load('compras.csv', [str, str, int, str, int, int, str])

credito_ano_homens = {}

for line in data:
    if line['pagamento'] == 'credito' and line['sexo'] == 'M':
        ano = line['ano']
        if ano not in credito_ano_homens:
            credito_ano_homens[ano] = 0
        credito_ano_homens[ano] += 1

maior_compra_credito_homens = -1
ano_maior_compra_credito_homens = 0

for chave, valor in credito_ano_homens.items():
    if valor > maior_compra_credito_homens:
        maior_compra_credito_homens = valor
        ano_maior_compra_credito_homens = chave

print(f"Ano em que os homens mais usaram crédito: {ano_maior_compra_credito_homens}")
