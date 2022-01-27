num = int(input('Digite um valor < 1000: '))
centena = num//100
dezena = ((num-centena*100)//10)
unidade = num % 10

txt_centena = 'centena'
txt_dezena = 'dezena'
txt_unidade = 'unidade'

txt_final = ''

if(centena > 0):
    if(centena > 1):
        txt_centena = 'centenas'
    txt_final = '%d ' % centena + txt_centena + ' '

if(dezena > 0):
    if(dezena > 1):
        txt_dezena = 'dezenas'
    txt_final += '%d ' % dezena + txt_dezena + ' '

if(unidade > 0):
    if(unidade > 1):
        txt_unidade = 'unidades'
    txt_final += '%d ' % unidade + txt_unidade

print(txt_final)
