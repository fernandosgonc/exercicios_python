# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

while True:
    nome = input('Digite seu nome: ')

    if(nome == ''):
        print('Não recebemos nada, tente novamente')
        continue

    else:
        # nome = nome.upper()

        tam_nome = len(nome)

        for i in range(tam_nome):
            print(nome[i])
        break
