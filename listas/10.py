# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor_um = list()
vetor_dois = list()
vetor_tres = list()

j = 0
while j < 2:
    print(f'------Vetor {j+1}')
    i = 0
    while i<10:

        numero = None
        try:
            numero = int(input('Digite o valor a ser inserido: '))
            if j == 0:
                vetor_um.append(numero)
            else:
                vetor_dois.append(numero)
        except: # pylint: disable=W0702
            print('Formato inválido. Tente novamente.')
            continue

        i += 1

    j += 1


k = 0
while k < 10:
    v_aux = [vetor_um[k], vetor_dois[k]]
    vetor_tres += (v_aux)
    k += 1

print(vetor_tres)