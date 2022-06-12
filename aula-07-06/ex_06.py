# Construa um programa que permita a um usuário informar uma série de números, 
# até que um número negativo seja fornecido. Ao final, imprima o somatório desses números, 
# a média, o valor máximo e o mínimo. Desconsidere o último número (negativo) informado pelo usuário.

sexo = input("Digite seu sexo: \nF -> Feminino\nM -> Masculino")
altura = float(input("Digite sua altura: "))

dados = []

estatisticas = {
    'homens': {
        'acima': 0,
        'abaixo': 0
    },
    'mulheres': {
        'acima': 0,
        'abaixo': 0
    }
}

while altura >= 0:
    dados.append(
        {
            'sexo': sexo,
            'altura': altura
        }
    )
    sexo = input("Digite seu sexo: \nF -> Feminino\nM -> Masculino")
    altura = float(input("Digite sua altura: "))

for i in dados:
    if i.sexo == 'F':
        if i.altura >= 1.6:
            estatisticas['mulheres']['acima'] += 1
        else:
            estatisticas['mulheres']['abaixo'] += 1
    else:
        if i.altura >= 1.6:
            estatisticas['homens']['acima'] += 1
        else:
            estatisticas['homens']['abaixo'] += 1

print(dados)