# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

while True:
    nome = input('Digite seu nome: ')

    if(nome == ''):
        print('Não recebemos nada, tente novamente')
        continue

    else:
        nome = nome.upper()

        tam_nome = len(nome)

        for i in range(1, tam_nome+1):
            for j in range(i):
                print(f'{nome[j]}', end='')
            print()
        break
