# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

idades = list()
alturas = list()

idades_inv = list()
alturas_inv = list()

i = 0
while i<5:

    idade = None
    altura = None
    try:
        idade = int(input(f'Digite a idade da pessoa {i+1}: '))
        altura = float(input(f'Digite a altura da pessoa {i+1}: '))
    except: # pylint: disable=W0702
        print('Algum dos dados é inconsistente. Tente novamente')
        continue

    idades.append(idade)
    alturas.append(altura)

    i += 1

j = -1
while j>-6:
    idades_inv.append(idades[j])
    alturas_inv.append(alturas[j])
    j -= 1

print('Normal: ')
print(f'Idades: {idades}\nAlturas: {alturas}')
print('Inverso: ')
print(f'Idades: {idades_inv}\nAlturas: {alturas_inv}')