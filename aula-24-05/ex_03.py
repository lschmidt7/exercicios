print("Qual o valor de compra do produto?")
valor = int(input())

if valor < 50:
    valor = valor + valor * 0.45
else:
    valor = valor + valor * 0.3

print("Valor de venda: {}".format(valor))