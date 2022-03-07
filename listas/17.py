# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m

nomes_atletas = list()
saltos = list()
saltos_medias = list()
extenso_saltos = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']

while True:
    nome_atleta = input('Nome do participante: ')
    if not nome_atleta:
        break

    nomes_atletas.append(nome_atleta)

    conj_saltos = list()
    i = 0
    while len(conj_saltos) < 5:
        salto = None
        try:
            salto = float(input(f'Valor do salto {i+1}: '))
        # pylint: disable = bare-except
        except:
            print('Formato invalido. Tente novamente.')
            continue

        conj_saltos.append(salto)
        i += 1

    saltos.append(conj_saltos)

    media = sum(conj_saltos)/len(conj_saltos)
    saltos_medias.append(media)

print()
print('************** RESULTADOS ********************')
for i in range(len(nomes_atletas)):
    print(f'Atleta: {nomes_atletas[i]}')
    j = 0
    for salto in saltos[i]:
        print(f'{extenso_saltos[j]} salto: {salto}')
        j += 1
    print('Resultado final: ')
    print(f'Nome do atleta: {nomes_atletas[i]}')
    print(f'Média dos saltos: {saltos_medias[i]:.2f}')
    print('-----------------------------------------------')
