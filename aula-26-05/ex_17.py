op = int(input("1 - Fahrenheit para Celsius\n2 - Celsius para Fahrenheit\n"))

if op == 1:
    temp_fahrenheit = int(input("Informe a temperatura em Fahrenheit: "))
    temp_celcius = 5 * (temp_fahrenheit - 32) / 9
    print("Temperatura em Celcius: {}".format(temp_celcius))
else:
    temp_celcius = int(input("Informe a temperatura em Celcius: "))
    temp_fahrenheit = 9 / 5 * temp_celcius + 32
    print("Temperatura em Fahrenheit: {}".format(temp_fahrenheit))