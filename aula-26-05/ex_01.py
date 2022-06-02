print("Digite o primeiro número: ")
n1 = int(input())

print("Digite o segundo número: ")
n2 = int(input())

print("Digite a opção desejada: \n1 - Soma \n2 - Subtração")
opcao = int(input())

resultado = 0

if opcao == 1:
    resultado = n1 + n2
    print("Resultado: {}".format(resultado))
elif opcao == 2:
    resultado = n1 - n2
    print("Resultado: {}".format(resultado))
else:
    print("Opção não existe")

