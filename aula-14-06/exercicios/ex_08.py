# A opção de débito é mais utilizada entre homens ou mulheres?

from Dados import load

header, data = load('compras.csv', [str, str, int, str, int, int, str])

debito = {
    'M': 0,
    'F': 0
}

for line in data:
    if line['pagamento'] == 'debito':
        sexo = line['sexo']
        debito[sexo] += 1

if debito['M'] > debito['F']:
    print('Débito é mais utilizado entre homens')
else:
    print('Débito é mais utilizado entre mulheres')