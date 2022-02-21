# Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

while True:
    nome = input('Digite seu nome: ')

    if(nome == ''):
        print('Não recebemos nada, tente novamente')
        continue

    else:
        nome = nome.upper()

        tam_nome = len(nome)

        for i in range(tam_nome-1, -1, -1):
            print(nome[i], end='')
        break
