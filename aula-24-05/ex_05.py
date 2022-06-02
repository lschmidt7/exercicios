n1 = int(input("Digite o primeiro número: "))

n2 = int(input("Digite o segundo número: "))

n3 = int(input("Digite o terceiro número: "))

if n1 + n2 == n3 or n2 + n3 == n1 or n3 + n1 == n2:
    print("A soma de dois dos números resulta no terceiro")