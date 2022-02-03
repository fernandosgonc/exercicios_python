def pega_float(msg):
    retorno = float(input(msg))
    return retorno


def pega_int(msg):
    retorno = int(input(msg))
    return retorno


def pega_txt(msg):
    retorno = str(input(msg))
    return retorno


print('Simulador de populações: ')
pais_A = pega_int('População país A: ')
pais_B = pega_int('População país B: ')
taxa_A = pega_float('Taxa de cresimento A: ')/100
taxa_B = pega_float('Taxa de crescimento B: ')/100

while(not(pais_A > 0 and pais_B > 0)):
    print('Valores invalidos para as populações. Tente novamente. ')
    pais_A = pega_int('População país A: ')
    pais_B = pega_int('População país B: ')

menor = 0
maior = 0
a_menor = False
b_menor = False
if(pais_A < pais_B):
    menor = pais_A
    maior = pais_B
    a_menor = True
else:
    b_menor = True
    menor = pais_B
    maior = pais_A

count_anos = 0
while(menor < maior):
    pais_A += pais_A*taxa_A
    pais_B += pais_B*taxa_B

    if(a_menor):
        menor = pais_A
        maior = pais_B
    else:
        menor = pais_B
        maior = pais_A

    count_anos += 1


if(a_menor):
    print(f'Em {count_anos} anos a população de A alcança a de B, tendo {pais_A} e {pais_B} habitantes, respectivamente')
else:
    print(f'Em {count_anos} anos a população de B alcança a de A, tendo {pais_B} e {pais_A} habitantes, respectivamente')


