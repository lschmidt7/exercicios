
lista_1 = []
lista_2 = []

for i in range(10):
    num = int(input("Digite um valor: "))
    lista_1.append(num)

for i in range(10):
    num = int(input("Digite um valor: "))
    lista_2.append(num)

lista_3 = []

for i in range(10):
    lista_3.append(lista_1[i])
    lista_3.append(lista_2[i])

print(lista_3)