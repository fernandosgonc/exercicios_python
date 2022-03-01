# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.


numeros = list()

while len(numeros)<10:

    numero = None
    try:
        numero = int(input('Digite o valor a ser inserido: '))
        numeros.append(numero)
    except: # pylint: disable=W0702
        print('Formato inválido. Tente novamente.')
        continue

soma = sum(numeros)

squares = list()
for value in numeros:
    value = (value**2)
    squares.append(value)

sum_sq = sum(squares)

print(f'Soma normal: {soma}, Soma quadrados: {sum_sq}')