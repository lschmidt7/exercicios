
segundos = int(input('Informe o tempo em segundos: '))

horas = int(segundos / 3600)

segundos -= horas * 3600

minutos = int(segundos / 60)

segundos -= minutos * 60

horas = horas if horas >= 10 else f'0{horas}'
minutos = minutos if minutos >= 10 else f'0{minutos}'
segundos = segundos if segundos >= 10 else f'0{segundos}'

print(f'{horas}:{minutos}:{segundos}')