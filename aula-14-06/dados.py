import csv

def ler_dados(nome_arquivo):
    # leitura do arquivo
    f = open(nome_arquivo, encoding='utf-8')
    dados = csv.reader(f, delimiter=',')
    dados = list(dados)
    return dados

def converter_para_dicionario(dados):
    quantidade_registros = len(dados)
    info = []
    for i in range(1,quantidade_registros):
        info.append(
            {
                'nome': dados[i][0],
                'sobrenome': dados[i][1],
                'idade': int(dados[i][2]),
                'sexo': dados[i][3],
                'compra': float(dados[i][4]),
                'ano': int(dados[i][5]),
                'pagamento': dados[i][6]
            }
        )
    return info