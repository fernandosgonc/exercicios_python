date = input('Digite uma data no formato dd/mm/aaaa: ')

dia = int(date[:2])
mes = int(date[3:5])
ano = int(date[6:])

print(ano)
ano_bissexto = (ano%4 == 0 and ano%100 != 0 or ano%400 == 0)
print('Bissexto: %r' %ano_bissexto)

data_valida = True

if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    
    if(dia < 1 or dia >31):
        data_valida = False
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):

    if(dia<1 or dia>30):
        data_valida = False

else:
    if not ano_bissexto:
        if(dia<1 or dia>28):
            data_valida = False
    else:
        if(dia<1 or dia>29):
            data_valida = False

if(data_valida):
    print('Data válida!')
else:
    print('Data inválida!')
