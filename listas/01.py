# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = list()
i = 0
while i < 5:
    num = input('Digite o valor a ser inserido: ')
    num = int(num)
    vetor.append(num)
    i += 1

print(vetor)
