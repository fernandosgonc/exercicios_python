def pega_float(msg):
    retorno = float(input(msg))
    return retorno


def pega_int(msg):
    retorno = int(input(msg))
    return retorno


def pega_txt(msg):
    retorno = str(input(msg))
    return retorno

# nota = 0
# while nota<1 or nota>10:
#     nota = pega_int('Digite um numero entre 1 e 10: ')
# print(f'O número digitado foi: {nota}')

# user = pega_txt('Username: ')
# password = pega_txt('Password: ')

# while(user.lower() == password.lower()):
#     print('User and password can not be the same. Try again')
#     user = pega_txt('Username: ')
#     password = pega_txt('Password: ')
# print('Signed up successfully')

# nome = pega_txt('Nome: ')
# idade = pega_int('Idade: ')
# salario = pega_float('Salario: ')
# sexo = pega_txt('Sexo: ')
# estado_civil = pega_txt('Estado civil: ')

# nome_valido = len(nome) >= 3
# idade_valida = idade>=0 and idade<=150
# salario_valido = salario>0
# sexo_valido = sexo.lower() == 'f' or sexo.lower() == 'm'
# estado_civil_valido = estado_civil.lower() == 's' or estado_civil.lower() == 'c' or estado_civil.lower() == 'v' or estado_civil.lower() == 'd'

# while(not(nome_valido and idade_valida and salario_valido and sexo_valido and estado_civil_valido)):
#     print('Alguma informação não está de acordo com o esperado. Tente novamente.')

#     nome = pega_txt('Nome: ')
#     idade = pega_int('Idade: ')
#     salario = pega_float('Salario: ')
#     sexo = pega_txt('Sexo: ')
#     estado_civil = pega_txt('Estado civil: ')

# print('Cadastro realizado!')

# pais_A = 80000
# pais_B = 200000
# taxa_A = 0.03
# taxa_B = 0.015

# count_anos = 0
# while(pais_A<pais_B):
#     pais_A += pais_A*taxa_A
#     pais_B += pais_B*taxa_B
#     count_anos += 1

# print(f'Em {count_anos} anos a população de A alcança a de B, tendo {pais_A} e {pais_B} habitantes, respectivamente')

# i = 0
# while i<20:
#     print(i, end = ' ')
#     i+=1

# print()

# maior = 0
# i = 0
# while( i < 5):
#     num = pega_float(f'Num {i+1}: ')
#     if(num>maior):
#         maior = num
#     i += 1
# # print(f'Maior: {maior}')

# # sum = 0
# # media = 0
# # i = 0
# # while(i < 5):
# #     num = pega_float(f'Num {i+1}: ')
# #     sum += num
# #     i += 1
# # media = sum/5
# # print(f'Some: {sum}, Media: {media}')

# # i = 1
# # while(i<=50):
# #     if(i%2 != 0):
# #         print(i, end =' ')
# #     i += 1
# # print()

# num_um = pega_int('Num 1: ')
# num_dois = pega_int('Num 2: ')
# sum = 0

# if(num_um<num_dois):
#     while(num_um<=num_dois):
#         print(num_um, end = ' ')
#         sum += num_um
#         num_um += 1


# elif (num_dois<num_um):
#     while(num_dois<=num_um):
#         print(num_dois, end = ' ')
#         sum += num_dois
#         num_dois += 1
# else:
#     print(num_um)
# print(f'Soma: {sum}')

# num = pega_int('Qual tabuada deseja? ')
# i = 1
# while(i<=10):
#     print(f'{num} x {i} = {num*i}')
#     i += 1

# base = pega_float('Base: ')
# exp = pega_float('Expoente: ')
# print(f'Potência: {base**exp}')

# count_par = 0
# count_impar = 0
# i = 0
# while(i<10):
#     num = pega_int(f'Num {i+1}: ')
#     if(num%2 == 0):
#         count_par += 1
#     else:
#         count_impar += 1
    
#     i += 1

# print(f'Pares: {count_par}, Impares: {count_impar}')

# a0 = 0
# a1 = 1
# n = pega_int('Quantidade de termos: ')
# i = 1
# while(i<=n):
#     while(a0<=500):

#         print(f'{a0},', end = ' ')
#         termo = a0 + a1
#         a0 = a1
#         a1 = termo

#     i += 1
    
# fat = pega_int('Fatorial de quem? ')
# i = fat
# while(i>1):
    
#     i -= 1
#     fat = (fat*i)
#     print(f'i: {i}, fat: {fat}')
# print(fat)


# num = pega_float('Num: ')
# while(True):
#     is_num_valid = (num > 0 and num <= 1000)
#     print(f'state: {is_num_valid}')
#     if(is_num_valid):
#         print('vai breakar')
#         break
#     num = pega_float('Invalido, tente novamente: ')
# print('Foi')


# def acha_fatorial(num):

#     i = num
#     while(i>1):
    
#         i -= 1
#         num = (num*i)
#     return num

# value = input('Qual o fatorial: ')
# while(True):
#     if(value.lower() == 'q'):
#         break

#     num_fat = int(value)
#     if(num_fat>0 and num_fat<16):
#         fat = acha_fatorial(num_fat)    
#         print(f'Fatorial de {num_fat} é: {fat}')
#     else:
#         print('Valor invalido, tente novamente: ')
    
#     value = input('Próximo: ')


num = pega_int('Digite o numero que deseja verificar se é primo: ')
while True:
    if(num<=1):
        num = pega_int('Invalido: ')
        continue

    i = 2
    count = 0
    while(i<=num/2):
        if(i != 1 and num%i == 0):
            count += 1
        i +=1
    break

if count>0:
    print('Não é primo')
else:
    print('É primo')