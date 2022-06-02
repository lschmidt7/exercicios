peso = float(input("Informe o peso do produto (em Kg): "))

preco = 0

if peso <= 0.5:
    preco = 1.1
elif peso > 0.5 and peso <= 2:
    preco = 2.2
elif peso > 2 and peso <= 10:
    preco = 3.7
else:
    extra = (peso - 10)
    extra = extra - extra % 1
    preco = 5 + extra * 3.8

print("Preço da encomenda: R$ {}".format(preco))