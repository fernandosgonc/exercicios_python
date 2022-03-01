# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.


numeros = list()

while len(numeros)<5:

    numero = None
    try:
        numero = int(input('Digite o valor: '))
    except: # pylint: disable=W0702
        print('Formato invalido. Tente novamente.')
        continue

    numeros.append(numero)

prod = 1
for value in numeros:
    prod *= value

print(numeros)
print(f'Soma: {sum(numeros)}, Produto: {prod}')