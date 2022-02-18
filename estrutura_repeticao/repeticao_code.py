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


# num = pega_int('Digite o numero que deseja verificar se é primo: ')
# while True:
#     if(num<=1):
#         num = pega_int('Invalido: ')
#         continue

#     i = 2
#     count = 0
#     while(i<=num/2):
#         print(f'Num {num}, i {i}')
#         if(num%i == 0):
#             count += 1
#             print(f'{num} é divisível por: {i}, ')
#         i +=1
#     break

# if count>0:
#     print('Não é primo')
# else:
#     print('É primo')

# n = pega_int('É primo? -> ')
# if (n == 1 or n == 2):
#     print('É primo, e não foram feitas nenhuma divisão.')
# elif(n % 2 == 0):
#     print('Não é primo, e foi feita 1 divisão.')
# else:
#     divisoes = 0
#     i = 3
#     primo = False
#     while(i<=n):
#         divisoes += 1
        
#         if(n%i == 0):
#             break
#         else:
#             primo = True
#         i += 2

# if primo:
#     print(f'Primo. {divisoes} divisões.')
# else:
#     print(f'Não é primo. {divisoes} divisões.')

# numero = int(input("Digite um numero inteiro: "))
# if numero == 1 or numero == 2:
#     print(
#         f"{numero} é primo e foram executadas 0 divisões para descobrir isso"
#     )
# elif numero % 2 == 0:
#     print(
#         f"{numero} não é primo e foi executada uma divisão para descobrir isso"
#     )
# else:
#     contador = 1
#     primo = True
#     for i in range(3, numero, 2):
#         print(f'I: {i}, numero: {numero}')
#         contador += 1
#         if numero % i == 0:
#             primo = False
#             break
#     if primo:
#         print(
#             f"{numero} é primo e foram executadas"
#             f" {contador} divisões para descobrir isso"
#         )
#     else:
#         print(
#             f"{numero} não é primo e foram executadas"
#             f" {contador} divisões para descobrir isso")

# n = pega_int('Quantas notas serão registradas? ')
# i = 0
# sum = 0
# while(i<n):
#     nota = pega_float(f'Nota {i+1}: ')
#     sum += nota
#     i += 1 
# media = sum/n
# print(f'A soma das notas é {sum}, e a média é {media:.2f}')

# n = pega_int('Quantas pessoas?')
# sum = 0
# for i in range(n):
#     idade = pega_int('Qual a idade? ')
#     sum += idade
# media = sum/n
# faixa_etaria = ''
# if(media<=25):
#      faixa_etaria = 'Jovem'
# elif(media <=60):
#     faixa_etaria = 'Adulta'
# else:
#     faixa_etaria = 'Idosa'
# print(f'A turma é {faixa_etaria}')

# qtd_eleitores = pega_int('Quantos eleitores? ')
# votos_cd_um = 0
# votos_cd_dois = 0
# votos_cd_tres = 0
# votos_brancos_nulos = 0

# for i in range(qtd_eleitores):
#     voto = pega_int('Digite seu voto: ')
#     voto_valido = False
#     while(not voto_valido):
#         if(voto == 1):
#             votos_cd_um += 1
#             voto_valido = True
#         elif(voto == 2):
#             voto_valido = True
#             votos_cd_dois += 1
#         elif(voto == 3):
#             voto_valido = True
#             votos_cd_tres += 1
#             voto_valido = True
#         elif(voto == 0):
#             voto_valido = True
#             votos_brancos_nulos += 1
#         else:
#             voto = pega_int('Invalido, tente novamente: ')

# print(f'Cd um: {votos_cd_um}, Cd dois: {votos_cd_dois}, Cd tres: {votos_cd_tres}')

# print('Loja Quase Dois - Tabela de preços')
# preco = 1.99
# for i in range(1, 51):
#     print(f'{i} - R$ {i*preco}')

# while True:
#     preco_produto = -1
#     while(preco_produto != 0):
#         cod_produto = 1
#         total = 0
#         preco_produto = pega_float(f'Produto {cod_produto}: R$ ')
#         total += preco_produto
#         cod_produto += 1
        
#         if(preco_produto == 0):
#             dinheiro = pega_float('Dinheiro: R$ ')
#             troco = dinheiro - total
#             print(f'Troco: R$ {troco}\n')
#             break
    

# salario_inicial = 1000
# aumento = 0.015
# ano_base = 1995
# ano_atual = 2022
# salario_atual = salario_inicial
# while(ano_base<=ano_atual):
#     print(f'Salario em {ano_base}: R$ {salario_atual}; aumento de {aumento}%')
#     salario_atual = salario_atual+(salario_atual*aumento)
#     ano_base += 1

#     if(ano_base>=1997):
#         aumento = aumento*2


# cod_aluno = pega_int('Codigo do aluno: ')
# altura_aluno = pega_float('Altura do aluno: ')
# maior_altura = altura_aluno
# cod_mais_alto = cod_aluno
# menor_altura = altura_aluno
# cod_mais_baixo = cod_aluno
# i = 1
# while(i<10):
#     cod_aluno = pega_int('Codigo do aluno: ')
#     altura_aluno = pega_float('Altura do aluno: ')

#     if(altura_aluno > maior_altura):
#         maior_altura = altura_aluno
#         cod_mais_alto = cod_aluno

#     if(altura_aluno < menor_altura):
#         menor_altura = altura_aluno
#         cod_mais_baixo = cod_aluno


#     i += 1
# print(f'Mais alto: {cod_mais_alto}, altura: {maior_altura}')
# print(f'Mais baixo: {cod_mais_baixo}, altura: {menor_altura}')

# valor_divida = pega_float('Valor da divida: ')
# qtd_parcelas = pega_int('Quantidade de parcelas: ')
# valor_juros = None
# if qtd_parcelas == 1:
#     valor_juros = 0
# elif qtd_parcelas == 3:
#     valor_juros = valor_divida*0.1
# elif qtd_parcelas == 6:
#     valor_juros = valor_divida*0.15
# elif qtd_parcelas == 9:
#     valor_juros = valor_divida*0.2
# else:
#     valor_juros = valor_divida*0.25

# valor_parcela = (valor_divida+valor_juros)/qtd_parcelas
# print('{:<10} {:<15} {:<15} {:<10}'.format('Valor da dívida', 'Valor dos juros', 'Qtd. Parcelas', 'Valor Parcela'))
# print('{:<15} {:<15} {:<15} {:<15}'.format(valor_divida, valor_juros, qtd_parcelas, valor_parcela))

# total = 0
# str_pedidos = ''


# while True:
    
#     cod_produto = pega_int('Digite o codigo do produto ')
#     if cod_produto == 0:
#         break
#     qtd = pega_int('Quantas unidades você deseja? ')
#     preco = 0

#     if cod_produto == 100 or cod_produto == 103:
#         preco = 1.2
#     elif cod_produto == 101 or cod_produto == 104:
#         preco = 1.3
#     elif cod_produto == 102:
#         preco = 1.5
#     elif cod_produto == 105:
#         preco = 1
#     else:
#         print('Codigo invalido, tente novamente.')
#         continue

#     valor_parcial = qtd*preco
#     str_pedidos += f'Cod: {cod_produto} ---- Qtd: {qtd} -------------- R$ {valor_parcial}\n'
#     total += valor_parcial

# str_pedidos += f'Total: ---------------------------- R$ {total:.2f}'
# print(str_pedidos)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# VOLTAR PARA FAZER USANDO DICIONÁRIO
# qtd_questoes = pega_int('Quantas questoes? ')
# i = 1
# gabarito = ''
# while(i<=qtd_questoes):
#     gabarito += input(f'Questão {i}, resposta: ')
#     gabarito += ' '
#     i += 1

while True:

    nome_atleta = input('Qual o nome do atleta? ')
    if(nome_atleta == '0'):
        break

    str_notas = ''
    melhor_nota = 0
    pior_nota = 10
    sum = 0
    for i in range(7):
        nota = pega_float(f'Nota {i+1}: ')
        sum += nota

        str_notas += 'Nota: ' + str(nota)

        if nota > melhor_nota:
            melhor_nota = nota
        if nota < pior_nota:
            pior_nota = nota
        
    media = (sum-melhor_nota-pior_nota)/7
    print('Resultado final:')
    print(f'Atleta: {nome_atleta}')
    print(f'Melhor nota: {melhor_nota}')
    print(f'Pior nota: {pior_nota}')
    print(f'Média: {media}')


# numero = input('Digite o numero inteiro que deseja inverter: ')
# index = len(numero)-1
# while(index>=0):
#     print(numero[index], end = '')
#     index -= 1

# n = pega_int('N: ')
# m = 1
# total = 0
# aux = 1
# while aux<=n:
#     print(f'{aux}/{m},', end = ' ')
#     total += aux/m
#     aux += 1
#     m += 2

# print(f'Total: {total}')

# n = pega_int('N: ')
# aux = 1
# h = 0
# while aux <= n:
#     print(f'1/{aux}, ', end = ' ')
#     h += 1/aux
#     aux += 1
# print(f'Total: {h}')

