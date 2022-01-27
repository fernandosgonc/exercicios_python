import math


def pega_teclado(msg):
    retorno = float(input(msg))
    return retorno

print('Alo mundo!')

print('---------------------')

numero = float(input('Digite um numero: '))
print('O número informado foi: %g'%numero)

print('---------------------')

print('Digite dois numeros a serem somados: ')
nmrA = float(input())
nmrB = float(input())
sum = nmrA+nmrB
print('%g + %g = %g'%(nmrA, nmrB, sum))

print('---------------------')

print('Digite as 4 notas bimestrais: ')
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))
media = (nota1+nota2+nota3+nota4)/4
print('A nota média é: %g'%media)


print('---------------------')

print('Conversor de medidas\nDigite a medida em metros')
metros = float(input())
cm = metros*100
print('%gm equivalem a %gcm'%(metros, cm))

print('---------------------')

raio = float(input('Digite o raio do círculo: '))
area = raio*raio*math.pi
print('A área do círculo é: %.3g'%area)

print('---------------------')

lado = float(input('Digite o tamanho da aresta do quadrado'))
areaQuadrado = lado*lado
print('A área do qudrado é %gu.m, e seu dobro é %gu.m' %(areaQuadrado,(areaQuadrado*2)))


print('---------------------')

taxaHora = pega_teclado('Digite o valor de sua hora de trabalho: ')
horasTrabalhadas = pega_teclado('Digite quantas horas trabalhou: ')
salario = taxaHora*horasTrabalhadas
print('Seu salário esse mês será de R$%g' %salario)

print('---------------------')

fahrenheit = pega_teclado('Digite a temperatura em ºF: ')
celsius = 5 * ((fahrenheit-32) / 9)
print('%gºF equivalem a %gºC' %(fahrenheit,celsius))


print('---------------------')


c = pega_teclado('Digite a temperatura em ºC: ')
f = (c*(9/5))+32
print('%gºC equivalem a %gºF' %(c,f))


print('---------------------')

intA = pega_teclado('Primeiro inteiro: ')
intB = pega_teclado('Segundo inteiro: ')
realC = pega_teclado('Numero real: ')
op_um = intA*(intB/2)
op_dois = intA*3+realC
op_tres = realC**3
print('Operacao 1: %g\nOperacao 2: %g\nOperacao 3: %g' %(op_um, op_dois, op_tres))

print('---------------------')


altura = pega_teclado('Qual a altura?')
peso_ideal = (72.7*altura) - 58
print('O peso ideal para essa pessoa é: %g' %peso_ideal)

print('---------------------')


h = pega_teclado('Qual a altura?')
peso_ideal_h = (72.7*h) - 58
peso_ideal_m = (62.1*h) - 44.7
print('O peso ideal, a depender do gênero, é: \nHomens: %g\nMulheres: %g' %(peso_ideal_h,peso_ideal_m))

print('---------------------')


peso = pega_teclado('Qual o peso dos peixes?')
excesso = peso - 50
multa = 4.00*excesso
print('O valor da multa é R$%g' %multa)

print('---------------------')


taxaHora = pega_teclado('Digite o valor de sua hora de trabalho: ')
horasTrabalhadas = pega_teclado('Digite quantas horas trabalhou: ')

salario_bruto = taxaHora*horasTrabalhadas
inss = salario_bruto*0.08
ir = salario_bruto*0.11
sindicato = salario_bruto*0.08
descontos = inss+ir+sindicato
salario_liquido = salario_bruto-descontos

print('+ salário bruto: R$ %g\n- IR(11%%): R$ %g\n- INSS(8%%): R$ %g\n- Sindicato(5%%): R$ %g\n= Salário líquido: R$%g\n' %(salario_bruto, ir, inss, sindicato, salario_liquido))


print('---------------------')

area_pintura = pega_teclado('Qual a área em metros² a ser pintada?')
cobertura_lata = 18*3
qtd_latas = area_pintura//cobertura_lata+1
preco = qtd_latas*80
print('Serão necessárias %d latas, total R$%g' %(qtd_latas, preco))


print('---------------------')


area_pintura = pega_teclado('Qual a área em metros² a ser pintada?')
area_pintura = area_pintura+(area_pintura*0.1)

cobertura_lata = 18*6
cobertura_galao = 3.6*6

qtd_latas = area_pintura//cobertura_lata+1
qtd_galoes = area_pintura//cobertura_galao+1

parcial_latas = area_pintura//cobertura_lata
area_parcial_galoes = area_pintura%cobertura_lata
parcial_galoes = area_parcial_galoes//cobertura_galao+1

print("parcial latas %d, preco: %g" %(parcial_latas, (parcial_latas*80)))
print("parcial galoes %d, preco: %g" %(parcial_galoes, (parcial_galoes*25)))


preco_latas = qtd_latas*80
preco_galoes = qtd_galoes*25
preco_mix = (parcial_latas*80) + (parcial_galoes*25)
print('Unicamete latas:  %d latas, total R$%g' %(qtd_latas, preco_latas))
print('Unicamete galoes:  %d galoes, total R$%g' %(qtd_galoes, preco_galoes))
print('Mix:  %d latas e %d galoes, total R$%g' % (parcial_latas, parcial_galoes, preco_mix))


tamanho_arquivo = pega_teclado('Tamanho do arquivo em MB')
tamanho_arquivo_mb = tamanho_arquivo*8
velocidade_internet = pega_teclado('Velocidade da internet em Mbps')
tempo_segundos = tamanho_arquivo_mb/velocidade_internet
tempo_minutos = tempo_segundos/60
print("O seu download demorará cerca de %g minutos" %tempo_minutos)