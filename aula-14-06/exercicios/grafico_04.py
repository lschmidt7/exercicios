# Exiba o valor total de compras por modo de pagamento.

import matplotlib.pyplot as plt

from Dados import load

header, data = load('compras.csv', [str, str, int, str, int, int, str])

modo_pagamento = {
    'debito': 0,
    'credito': 0,
    'dinheiro': 0
}

for line in data:
    mp = line['pagamento']
    modo_pagamento[mp] += 1

x = modo_pagamento.keys()
y = modo_pagamento.values()

fig, ax = plt.subplots()
ax.bar(x, y)
plt.show()