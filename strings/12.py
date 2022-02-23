# Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

is_tel_valid = False
is_tel_corrected = False
while not is_tel_valid:

    telefone_inp = input('Digite o numero do telefone: ')
    telefone = telefone_inp.strip()
    telefone = telefone.replace('-', '')

    count = 0
    if len(telefone) >= 7 and len(telefone) <= 8:
        for char in telefone:
            if char.isdigit():
                count += 1
    else:
        print('Numero invalido, tente novamente.')
        continue

    if count == 7:
        telefone = '3' + telefone
        is_tel_corrected = True

    is_tel_valid = True

print(f'Telefone: {telefone_inp}')
if is_tel_corrected:
    print(f'Telefone possui 7 dígitos. Vou acrescentr o dígito três na frente.')
    print(f'Telefone corrigido sem formatação: {telefone}')
    print(f'Telefone corrigido com formatação: {telefone[:4]}-{telefone[4:]}')
