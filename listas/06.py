# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias = list()
medias_maiores_que_sete = list()

aluno = 0
while aluno < 10:

    notas = list()

    i = 0
    while i < 4:
        nota = None
        try:
            nota = float(input('Digite a nota: '))
        except:  # pylint: disable=W0702
            print('Formato invalido. Tente novamente.')
            continue

        notas.append(nota)
        i += 1

    media = sum(notas)/len(notas)
    medias.append(media)

    aluno += 1

for media in medias:
    if media >= 7:
        medias_maiores_que_sete.append(media)

print(f'{len(medias_maiores_que_sete)} alunos obtiveram média maior ou igual a 7.')
