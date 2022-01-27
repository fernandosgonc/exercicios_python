import math

def pega_teclado(msg):
    retorno = float(input(msg))
    return retorno


numero_1 = pega_teclado('Digite o primeiro numero: ')
numero_2 = pega_teclado('Digite o segundo numero: ')
maior = 0
if(numero_1 > maior):
    maior = numero_1
if(numero_2 > maior):
    maior = numero_2

print('O maior numero é %g' % maior)

valor = pega_teclado('Digite um numero ')
if(valor >= 0):
    print('É positivo')
else:
    print('É negativo')

letra = input('Digite uma letra')
if(letra == 'F' or letra == 'f'):
    print('Feminino')
elif(letra == 'M' or letra == 'm'):
    print('Masculino')
else:
    print('Bem vinde!')

letra = input('Digite uma letra: ')
if(letra == 'A' or letra == 'a'
   or letra == 'E' or letra == 'e'
   or letra == 'I' or letra == 'i'
   or letra == 'O' or letra == 'o'
   or letra == 'U' or letra == 'u'):
    print("É vogal!")
else:
    print("Consoante!")

nota_1 = pega_teclado('Nota 1: ')
nota_2 = pega_teclado('Nota 2: ')
media = nota_1+nota_2
media = media/2

if(media >= 7):
    print('Aprovado!')
elif(media == 10):
    print('Aprovado com distinção!')
else:
    print("Reprovado!")

numero_1 = pega_teclado('Digite o primeiro numero: ')
numero_2 = pega_teclado('Digite o segundo numero: ')
numero_3 = pega_teclado('Digite o terceiro numero: ')

maior = 0
if(numero_1 > maior):
    maior = numero_1
if(numero_2 > maior):
    maior = numero_2
if(numero_3 > maior):
    maior = numero_3
print('O maior numero é %g' % maior)

numero_1 = pega_teclado('Digite o primeiro numero: ')
numero_2 = pega_teclado('Digite o segundo numero: ')
numero_3 = pega_teclado('Digite o terceiro numero: ')

maior = numero_1
menor = numero_1

if(numero_2 > maior):
    maior = numero_2
if(numero_3 > maior):
    maior = numero_3

if(numero_2 < menor):
    menor = numero_2
if(numero_3 < menor):
    menor = numero_3


print('O maior numero é %g' % maior)
print('O menor numero é %g' % menor)

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


a = pega_teclado('Num 1: ')
b = pega_teclado('Num 2: ')
c = pega_teclado('Num 3: ')

if(a > b and a > c):
    if(b > c):
        print('A: %g, B: %g, C: %g' % (a, b, c))
    else:
        print('A: %g, C: %g, B: %g' % (a, c, b))
elif(b > a and b > c):
    if(a > c):
        print('B: %g, A: %g, C: %g' % (b, a, c))
    else:
        print('B: %g, C: %g, A: %g' % (b, c, a))
else:
    if(a > b):
        print('C: %g, A: %g, B: %g' % (c, a, b))
    else:
        print('C: %g, B: %g, A: %g' % (c, b, a))


salario_atual = pega_teclado('Digite seu salário atual: ')

reajuste = None
novo_salario = salario_atual
if (salario_atual <= 280):
    reajuste = 0.2
elif (salario_atual > 280 and salario_atual < 700):
    reajuste = 0.15
elif (salario_atual >= 700 and salario_atual < 1500):
    reajuste = 0.1
else:
    reajuste = 0.05

aumento = salario_atual*reajuste
novo_salario += aumento

print('Salário antes do reajuste: R$ %g' % salario_atual)
print('O valor do resjuste foi de %g%%' % reajuste)
print('O valor de aumento foi de R$ %g' % aumento)
print('O novo salário é R$ %g' % novo_salario)

lado_a = pega_teclado('Lado A: ')
lado_b = pega_teclado('Lado B: ')
lado_c = pega_teclado('Lado C: ')

is_triangle = False

if(lado_a+lado_b > lado_c
   or lado_a+lado_c > lado_b
   or lado_b+lado_c > lado_a):
    is_triangle = True

if(is_triangle):
    if(lado_a == lado_b and lado_b == lado_c):
        print("Triângulo Equilátero")
    if((lado_a == lado_b and lado_a != lado_c)
    or(lado_b == lado_c and lado_b != lado_a)):
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')
else:
    print("Não é triângulo")
    
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

ano = int(input('Digite o ano: '))
if(ano%4 == 0 and ano%100 != 0 or ano%400 == 0):
    print('É bissexto')
else:
    print('Não é bissexto')

num = pega_teclado('Digite o numero: ')
num = num*10
is_int = num%10 == 0

if(is_int):
    print('É inteiro')
else:
    print('É decimal')

combustivel = input('Qual o tipo de combustível? ')
qtd_litros = pega_teclado('Quantos litros?')

total = 0
desconto = 0
if(combustivel == 'A' or combustivel == 'G'):
    if(combustivel == 'A'):
        combustivel = 'Alcool'
        total = 2.5*qtd_litros
        if(qtd_litros<=20):
            desconto = 0.03
        else:
            desconto = 0.05

    elif(combustivel == 'G'):
        combustivel = 'Gasolina'
        total = 1.9*qtd_litros
        if(qtd_litros<=20):
            desconto = 0.04
        else:
            desconto = 0.06
else:
    print('Opção inválida!')

desconto = total*desconto


print('Combustível: %s'%combustivel)
print('Quantidade: %gL'%qtd_litros)
print('Preço total: R$ %g'%total)
print('Desconto: R$ %g'%desconto)
print('Valor a ser pago: R$ %g'%(total-desconto))