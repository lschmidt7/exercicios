
rio = 0
bahia = 0
minas = 0

for i in range(10):
    nome = input("Informe seu nome: ")
    destino = int(input("Informe o local para onde você já viajou?\n1 - Rio de Janeiro\n2 - Bahia\n3 - Minas Gerais"))
    if destino == 1:
        rio += 1
    elif destino == 2:
        bahia += 1
    elif destino == 3:
        minas += 1

if rio > bahia and rio > minas:
    print("Destino mais visitado: Rio de Janeiro")
elif bahia > rio and bahia > minas:
    print("Destino mais visitado: Bahia")
elif minas > bahia and minas > rio:
    print("Destino mais visitado: Minas Gerais")