def pega_teclado(msg):
    retorno = float(input(msg))
    return retorno


a = pega_teclado('Num 1: ')
b = pega_teclado('Num 2: ')
c = pega_teclado('Num 3: ')

if(a < b and a < c):
    if(b < c):
        print('A: %g, B: %g, C: %g' % (a, b, c))
    else:
        print('A: %g, C: %g, B: %g' % (a, c, b))
elif(b < a and b < c):
    if(a < c):
        print('B: %g, A: %g, C: %g' % (b, a, c))
    else:
        print('B: %g, C: %g, A: %g' % (b, c, a))
else:
    if(a < b):
        print('C: %g, A: %g, B: %g' % (c, a, b))
    else:
        print('C: %g, B: %g, A: %g' % (c, b, a))
