segundos = int(input("Informe a quantidade de segundos: "))

if segundos > 86400:
    dias = int(segundos / 86400)
    print(f"Dias equivalentes: {dias}")
elif segundos > 3600:
    horas = int(segundos / 3600)
    print(f"Horas equivalentes: {horas}")
else:
    minutos = int(segundos / 60)
    print(f"Minutos equivalentes: {minutos}")
