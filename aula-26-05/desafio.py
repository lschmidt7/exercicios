from random import randint

n1 = int(input("Informe o primeiro número do palpite: "))
n2 = int(input("Informe o sefgundo número do palpite: "))
n3 = int(input("Informe o terceiro número do palpite: "))

na1 = randint(0,9)
na2 = randint(0,9)
na3 = randint(0,9)

if n1 == na1 and n2 == na2 and n3 == na3:
    print("Acertou todos os números em ordem")
elif (n1 + n2 + n3) - (na1 + na2 + na3) == 0 and (n1 != na1 or n2 != na2 or n3 != na3):
    print("Acertou todos os números mas não em ordem")
else:
    n1_hit = n1 == na1 or n1 == na2 or n1 == na3
    n2_hit = n2 == na1 or n2 == na2 or n2 == na3
    n3_hit = n3 == na1 or n3 == na2 or n3 == na3

    acertos = 0

    if n1_hit:
        acertos += 1
    if n2_hit:
        acertos += 1
    if n3_hit:
        acertos += 1

    print(f"Acertos: {acertos}")