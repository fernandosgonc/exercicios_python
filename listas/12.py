# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = list()
alturas = list()
media_altura = 0
count_alunos = 0

i = 0
while i < 30:

    idade = None
    altura = None
    try:
        idade = int(input(f'Digite a idade do aluno {i+1}: '))
        altura = float(input(f'Digite a altura do aluno {i+1}: '))

    except:  # except: pylint: disable = bare-except
        print('Algum dado é inválido, tente novamente.')
        continue

    idades.append(idade)
    alturas.append(altura)

    i += 1


media_altura = sum(alturas)/len(alturas)

j = 0
while j < 30:
    if idades[j] >= 13 and alturas[j] < media_altura:
        count_alunos += 1
    j += 1

print(
    f'A sala possui {count_alunos} com 13 anos ou menos, com altura menor que a média, de {media_altura:.2f}')
