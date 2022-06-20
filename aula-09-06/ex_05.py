# Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, 
# com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. 
# Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
# 8  3  4 
# 1  5  9
# 6  7  2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos 
# com as características acima. Dica: produza todas as combinações possíveis e verifique 
# a soma quando completar cada quadrado.

def soma_linha(quadrado, tamanho, l):
    soma = 0
    for c in range(tamanho):
        soma += quadrado[l][c]
    return soma

def soma_coluna(quadrado, tamanho, c):
    soma = 0
    for l in range(tamanho):
        soma += quadrado[l][c]
    return soma

def soma_diagonal_principal(quadrado, tamanho):
    soma = 0
    for d in range(tamanho):
        soma += quadrado[d][d]
    return soma

def soma_diagonal_secundaria(quadrado, tamanho):
    soma = 0
    for d in range(tamanho):
        soma += quadrado[d][tamanho - d - 1]
    return soma

def eh_quadrado(quadrado):
    quantidade_linhas = len(quadrado)
    valido = True
    for linha in quadrado:
        quantidade_colunas = len(linha)
        if quantidade_colunas != quantidade_linhas:
            valido = False
    return valido, quantidade_linhas

def quadrado_magico(quadrado):
    quadrado_valido, tamanho = eh_quadrado(quadrado)
    somas = []
    if quadrado_valido:
        for l in range(tamanho):
            soma = soma_linha(quadrado, tamanho, l)
            somas.append(soma)
        for c in range(tamanho):
            soma = soma_coluna(quadrado, tamanho, c)
            somas.append(soma)
        for d in range(tamanho):
            soma = soma_diagonal_principal(quadrado, tamanho)
            somas.append(soma)
        for d in range(tamanho):
            soma = soma_diagonal_secundaria(quadrado, tamanho)
            somas.append(soma)
        valor = somas[0]
        for soma in somas:
            if soma != valor:
                return False
        return True
    else:
        print('Não é um quadrado!')
        return False

quadrado = [
    [8, 3, 2],
    [1, 5, 9],
    [6, 7, 4]
]

resultado = quadrado_magico(quadrado)

print(resultado)