# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor = list()
vogais = ['a', 'e', 'i', 'o', 'u']
nao_vogais = list()
count_vogais = 0
while len(vetor)<10:

    value = input('Digite o caractere: ')
    vetor.append(value)

    if value.lower() in vogais:
        count_vogais += 1
    else:
        nao_vogais.append(value)

print(f'Vetor: {vetor}')
print(f'Quantidade de não-vogais: {len(vetor) - count_vogais}')
print(f'Não-vogais: {nao_vogais}')