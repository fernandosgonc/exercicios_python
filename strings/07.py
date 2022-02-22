# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.

frase = input('Digite a frase desejada: ')
frase = frase.strip()
sp_count = frase.count(' ')
a_count = frase.count('a')
e_count = frase.count('e')
i_count = frase.count('i')
o_count = frase.count('o')
u_count = frase.count('u')

print(f'Existem {sp_count} espaços em branco')
print(f'{a_count} letras A, {e_count} letras E, {i_count} letras I, {o_count} letras O, {u_count} letras U')