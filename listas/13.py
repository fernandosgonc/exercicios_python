#  Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas = list()
temperatura_media_anual = 0

mes_atual = 1
while len(temperaturas) < 12:

    temperatura = None
    try:
        temperatura = float(input(f'Digite a temperatura do mês {mes_atual}: '))
        mes_atual += 1
    # pylint: disable = bare-except
    except:
        print('Formato invalido, tente novamente.')
        continue

    temperaturas.append(temperatura)


temperatura_media_anual = sum(temperaturas)/len(temperaturas)

meses_mais_quentes = list()
indice_temp = 0
for temperatura in temperaturas:
    if temperatura > temperatura_media_anual:
        meses_mais_quentes.append(indice_temp)
    indice_temp += 1

meses_quentes_nomes = list()
for i in range(len(meses_mais_quentes)):
    numero_mes = meses_mais_quentes[i]
    meses_quentes_nomes.append(meses[numero_mes])

print(f'Media: {temperatura_media_anual}')
print(f'Meses mais quentes: {meses_mais_quentes}')
print(f'Meses mais quentes: {meses_quentes_nomes}')
