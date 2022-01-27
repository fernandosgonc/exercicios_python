import math

def pega_teclado(msg):
    retorno = float(input(msg))
    return retorno

print('Bhaskara')    
a = pega_teclado('Digite o valor de A: ')
b = pega_teclado('Digite o valor de B: ')
c = pega_teclado('Digite o valor de C: ')

is_valid = False

if a != 0:
    is_valid = True

delta = (b**2)-(4*a*c)

if(is_valid):
    raiz_um = ((b*-1)+math.sqrt(delta)) / (2*a)
    raiz_dois = ((b*-1)-math.sqrt(delta)) / (2*a)

    if delta > 0:
        print('Raiz um: %g' %raiz_um)
        print('Raiz dois: %g' %raiz_dois)
    elif delta == 0:
        print('Raiz única: %g' %raiz_um)
    else:
        print('Não possui raízes reais.')
else:
    print('Não é uma equação do segundo grau')
