# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

respostas = list()
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

print('INQUÉRITO. RESPONDA ÀS PERGUNTAS.')
for pergunta in perguntas:
    print(pergunta)

    resposta_valida = False
    while not resposta_valida:
        resposta = input()
        if resposta.lower().startswith('sim'):
            respostas.append(1)
            resposta_valida = True
        elif resposta.lower().startswith('nao'):
            respostas.append(0)
            resposta_valida = True
        else:
            print('Resposta invalida. Responda à pergunta com sim ou não!')

respostas_positivas = respostas.count(1)

classificacao = ''
if respostas_positivas == 5:
    classificacao = 'Assassino'
elif respostas_positivas >=3:
    classificacao = 'Cúmplice'
elif respostas_positivas == 2:
    classificacao = 'Suspeito'
else:
    classificacao = 'Inocente'

print(f'Você é um {classificacao}')