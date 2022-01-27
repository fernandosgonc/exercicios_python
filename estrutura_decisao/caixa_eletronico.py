valor = input('Quanto deseja sacar? ')
valor = int(valor)

centena = valor//100
dezena = (valor-(centena*100))//10
unidade = valor%10

notas_cem = centena
notas_cinquenta = 0
notas_dez = 0
notas_cinco = 0
notas_um = 0

if(dezena>=5):
    notas_cinquenta = 1
    notas_dez = dezena-5
else:
    notas_dez = dezena

if(unidade>=5):
    notas_cinco = 1
    notas_um = unidade-5
else:
    notas_um = unidade

if(centena>0):
    print('%d notas de cem' %notas_cem)

if(dezena>0):
    if(dezena>=5):
        print('%d notas de cinquenta' %notas_cinquenta)
    if(notas_dez!=0):
        print('%d notas de dez' %notas_dez)

if(unidade>0):
    if(unidade>=5):
        print('%d nota de cinco' %notas_cinco)
    if(notas_um!=0):
        print('%d notas de um' %notas_um)
