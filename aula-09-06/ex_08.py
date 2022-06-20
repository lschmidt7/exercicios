#Escreva uma função que conte o número de espaços em branco em uma frase passada como parâmetro.

frase = input('Digite uma frase: ')

espacos = 0

for c in frase:
    if c == ' ':
        espacos += 1

print(f'A frase contém {espacos} espaços em branco')