from random import randint

inicio_intervalo = int(input("Digite o inicio do intervalo: "))
fim_intervalo = int(input("Digite o fim do intervalo: "))
palpite = int(input("Digite o seu palpite: "))

numero_aleatorio = randint(inicio_intervalo, fim_intervalo)

if palpite == numero_aleatorio:
    print("Parabéns você acertou!")
elif palpite < numero_aleatorio:
    print("Palpite muito baixo!")
elif palpite > numero_aleatorio: # poderia ser um else aqui também
    print("Palpite muito alto!")