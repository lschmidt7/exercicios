# Construa um programa que permita a um usuário informar uma série de números, 
# até que um número negativo seja fornecido. Ao final, imprima o somatório desses números, 
# a média, o valor máximo e o mínimo. Desconsidere o último número (negativo) informado pelo usuário.

num = int(input("Digite um valor: "))

info = {
    'quantidade': 0,
    'somatorio': 0,
    'media': 0,
    'max': num,
    'min': num
}

while num >= 0:
    info['somatorio'] += num

    if num < info['min']:
        info['min'] = num
    if num > info['max']:
        info['max'] = num
    
    info['quantidade'] += 1

    num = int(input("Digite um valor: "))

info['media'] /= info['quantidade']

print(info)