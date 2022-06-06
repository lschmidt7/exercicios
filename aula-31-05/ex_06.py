votos_candidato_1 = 0
votos_candidato_2 = 0
nulos = 0
brancos = 0

for i in range(5):
    voto = int(input("Informe seu voto: \n1 - Candidato José\n2 - Candidata Maria\n3 - Nulo\n4 - Branco"))

    if voto == 1:
        votos_candidato_1 += 1
    elif voto == 2:
        votos_candidato_2 += 1
    elif voto == 3:
        nulos += 1
    elif voto == 4:
        brancos += 1

print(f"Candidato 1: {votos_candidato_1}")
print(f"Candidato 2: {votos_candidato_2}")
print(f"Nulos: {nulos}")
print(f"Brancos: {brancos}")