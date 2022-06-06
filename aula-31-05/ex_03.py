# E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + … + 1 / N!

n = int(input("Informe um número: "))

valor_e = 1

for i in range(1, n + 1):

    fatorial = 1
    for j in range(i, 1, -1):
        fatorial = fatorial * j
    
    valor_e += 1 / fatorial

print(f"E: {valor_e}")