import csv
from dados import ler_dados, converter_para_dicionario

nome_arquivo = 'compras.csv'

dados = ler_dados(nome_arquivo)

quantidade_registros = len(dados)

info = converter_para_dicionario(dados)

maior_compra = -1
indice_maior_compra = 0

header = dados[0]

for indice, linha in enumerate(info):
    if linha['compra'] > maior_compra:
        maior_compra = linha['compra']
        indice_maior_compra = indice

pessoa = info[indice_maior_compra]

print(f"{indice_maior_compra}: {pessoa['nome']} {pessoa['sobrenome']} compra no valor {pessoa['compra']}")