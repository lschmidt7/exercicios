# Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. 
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão 
# é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, 
# eles devem ser modificados para valores dentro da faixa.

# +---------------------+
# |                     |
# |                     |
# |                     |
# +---------------------+

linhas = int(input("Digite a quantidade de linhas"))
colunas = int(input("Digite a quantidade de colunas"))

retangulo = ''

for l in range(linhas):
    line = ''
    if l == 0 or l == linhas - 1: # verifica se está na primeira linha ou na última linha
        line += '+'
        for c in range(colunas):
            line += '-'
        line += '+'
    else:
        line += '|'
        for c in range(colunas):
            line += '*'
        line += '|'
    line += '\n'
    retangulo += line

print(retangulo)