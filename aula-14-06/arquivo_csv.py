import csv

nome_arquivo = 'dados.txt'
f = open(nome_arquivo, encoding='utf-8')

dados = csv.reader(f, delimiter=',')

print(list(dados))