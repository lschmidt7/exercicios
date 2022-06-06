# Janeiro   31 dias
# Fevereiro 28 dias (29 dias nos anos bissextos)
# Março	    31 dias
# Abril	    30 dias
# Maio	    31 dias
# Junho	    30 dias
# Julho	    31 dias
# Agosto    31 dias
# Setembro  30 dias
# Outubro	31 dias
# Novembro  30 dias
# Dezembro  31 dias

dia = int(input("Informe o dia do mês: "))
mes = int(input("Informe o mês do ano: "))
ano = int(input("Informe o ano: "))

ano_bissexto = ano % 4 == 0

novo_dia = dia + 1

novo_mes = mes
novo_ano = ano

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12: # 31 dias
    if novo_dia > 31:
        novo_dia = 1
        novo_mes = mes + 1
        if novo_mes > 12:
            novo_mes = 1
            novo_ano = ano + 1

elif mes != 2: # 30 dias
    if novo_dia > 30:
        novo_dia = 1
        novo_mes = mes + 1
        if novo_mes > 12:
            novo_mes = 1
            novo_ano = ano + 1
else: # fevereiro
    if ano_bissexto: # 29 dias
        if novo_dia > 29:
            novo_dia = 1
            novo_mes = mes + 1
            if novo_mes > 12:
                novo_mes = 1
                novo_ano = ano + 1
    else: # 28 dias
        if novo_dia > 28:
            novo_dia = 1
            novo_mes = mes + 1
            if novo_mes > 12:
                novo_mes = 1
                novo_ano = ano + 1

print("Próxima Data: {}/{}/{}".format(novo_dia, novo_mes, novo_ano))