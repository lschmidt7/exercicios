# Qual a porcentagem de homens e mulheres na base de dados?

from Dados import load

header, data = load('compras.csv', [str, str, int, str, int, int, str])

homens = 0
mulheres = 0

for line in data:
    if line['sexo'] == 'M':
        homens += 1
    else:
        mulheres += 1

total = homens + mulheres

perc_homens = homens / total * 100
perc_mulheres = mulheres / total * 100

print(f"Homens: {perc_homens}%")
print(f"Mulheres: {perc_mulheres}%")