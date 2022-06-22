# Qual a porcentagem de homens e mulheres na base de dados?

import matplotlib.pyplot as plt

from Dados import load

header, data = load('compras.csv', [str, str, int, str, int, int, str])

homens = 0
mulheres = 0

for line in data:
    if line['sexo'] == 'M':
        homens += 1
    else:
        mulheres += 1

fig, ax = plt.subplots()
ax.bar(['Homens', 'Mulheres'], [homens, mulheres])
plt.show()