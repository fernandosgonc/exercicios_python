# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = list()
while True:
    try:
        nota = float(input('Digite a nota: '))
    except: # pylint: disable=W0702
        print('Formato não aceito. Tente novamente.')
        continue

    notas.append(nota)
    if(len(notas)==4): break

media = sum(notas)/len(notas)
print(f'Soma das notas: {sum(notas)}, Média: {media}')