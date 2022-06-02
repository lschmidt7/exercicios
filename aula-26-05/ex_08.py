preco = 300

tipo_madeira = float(input("Informe o tipo de madeira: \n1 - Angelim\n2 - Pinus"))
numero_caracteres = int(input("Informe a quantidade de caracteres da frase: "))
letras_douradas = int(input("A placa possui quantas letras douradas?"))

if tipo_madeira == 1:
    preco += 150
if numero_caracteres > 12:
    preco += (numero_caracteres - 12) * 15

preco += letras_douradas * 60

print("Orçamento da placa: R$ {}".format(preco))