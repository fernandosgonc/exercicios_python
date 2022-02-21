# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.

str_um = input('String 1: ')
str_dois = input('String 2: ')

tam_str_um = len(str_um)
tam_str_dois = len(str_dois)

is_same_size = tam_str_dois == tam_str_um

print(f'String 1: {str_um}\nString 2: {str_dois}')
print(f'Tamanho de "{str_um}": {tam_str_um} caracteres')
print(f'Tamanho de "{str_dois}": {tam_str_dois} caracteres')

if(is_same_size):
    print('As duas strings possuem o mesmo tamanho')
else:
    print('As duas strings são de tamanhos diferentes.')

if(str_um == str_dois):
    print('As duas strings possuem o mesmo conteúdo')
else:
    print('As duas string possuem conteúdo diferente')