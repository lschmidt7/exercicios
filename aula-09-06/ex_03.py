# Construa uma função que receba uma data no formato DD/MM/AAAA e devolva
# uma string em um formato por extenso. Opcionalmente, valide a data e 
# retorne None caso a data seja inválida.

meses = ['Janeiro',
         'Fevereiro', 
         'Março', 
         'Abril', 
         'Maio', 
         'Junho', 
         'Julho', 
         'Agosto', 
         'Setembro', 
         'Outubro', 
         'Novembro', 
         'Dezembro']

data = input("Informe uma data no formatdo DD/MM/AAAA")

data = data.split('/')

dia, mes, ano = data

mes = int(mes)

print(f'Hoje: {dia} de {meses[mes]} de {ano}')