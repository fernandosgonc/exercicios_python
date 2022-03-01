# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

vetor = []
i = 0
while i<10:

    num = int(input('Digite o valor a ser inserido: '))
    vetor.append(num)
    i += 1

vetor_inv = []
j = len(vetor)-1
while j>=0:
    vetor_inv.append(vetor[j])
    j -= 1

print(vetor_inv)