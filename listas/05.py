# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = list()
pares = list()
impares = list()

while len(numeros)<20:

    numero = None
    try:
        numero = int(input('Digite o valor a ser inserido: '))
        numeros.append(numero)
    except: # pylint: disable=W0702
        print('Formato inválido. Tente novamente.')
        continue

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(numeros)
print(pares)
print(impares)