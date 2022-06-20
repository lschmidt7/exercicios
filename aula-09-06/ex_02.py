# Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, 
# e ‘N’, se seu argumento for zero ou negativo.

def positivo_negativo(valor):
    if valor < 0:
        return 'N'
    else:
        return 'P'

res = positivo_negativo(5)

print(res)

res = positivo_negativo(-2)

print(res)