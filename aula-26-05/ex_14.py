
temperatura = float(input("Informe a temperatura atual: "))

if temperatura <= 15:
    print("Muito frio")
elif 16 <= temperatura <= 22:
    print("Frio")
elif 23 <= temperatura <= 26:
    print("Agradável")
elif 27 <= temperatura <= 30:
    print("Quente")
else:
    print("Muito Quente")