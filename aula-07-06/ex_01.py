# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros = []

for i in range(10):
    x = float(input("Digite um número: "))
    numeros.append(x)

for i in range(9, -1, -1):
    print(numeros)