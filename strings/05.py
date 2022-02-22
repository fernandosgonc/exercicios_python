# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

# FULANO
# FULAN
# FULA
# FUL
# FU
# F

while True:
    nome = input('Digite seu nome: ')

    if(nome == ''):
        print('Não recebemos nada, tente novamente')
        continue

    else:
        nome = nome.upper()

        tam_nome = len(nome)

        for i in range(tam_nome, 0 , -1):
            for j in range(i):
                print(f'{nome[j]}', end='')
            print()
        break