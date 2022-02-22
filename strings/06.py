# Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

# Data de Nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.

def is_date_valid(date):

    dia = int(date[:2])
    mes = int(date[3:5])
    ano = int(date[6:])

    ano_bissexto = (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0)

    data_valida = True

    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):

        if(dia < 1 or dia > 31):
            data_valida = False
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):

        if(dia < 1 or dia > 30):
            data_valida = False

    else:
        if not ano_bissexto:
            if(dia < 1 or dia > 28):
                data_valida = False
        else:
            if(dia < 1 or dia > 29):
                data_valida = False

    return data_valida


isdatevalid = False
while not isdatevalid:

    date = input('Digite sua data de aniversário: ')

    dd = date[:2]
    mm = date[3:5]
    aaaa = date[6:]
    # print(f'dd {dd} mm {mm} a {aaaa}')

    if(dd.isdigit() and mm.isdigit() and aaaa.isdigit()):
        if(is_date_valid(date)):
            isdatevalid = True
        else:
            print('Data inválida. Tente novamente.')

    else:
        print('Caracteres invalidos, tente novamente.')

txt_mes = ''
if mm == '01':
    txt_mes = 'Janeiro'
elif mm == '02':
    txt_mes = 'Fevereiro'
elif mm == '03':
    txt_mes = 'Março'
else:
    txt_mes = 'Dezembro'
 
print(f'Você nasceu em {dd} de {txt_mes} de {aaaa}')