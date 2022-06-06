
maior_numero = 0
menor_numero = 0

for i in range(10):

    n = int(input("Informe um número: "))

    if i == 0:
        maior_numero = n
        menor_numero = n
    else:
        if n > maior_numero:
            maior_numero = n
        if n < menor_numero:
            menor_numero = n

print("Maior número: {}".format(maior_numero))
print("Menor número: {}".format(menor_numero))