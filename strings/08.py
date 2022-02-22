# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

palavra = input('Digite a palavra e verificaremos se é um palíndromo: ')

is_palindrome = True
i = 0
j = len(palavra)-1

while (i<len(palavra)-1) and (j>0):
    if(palavra[i] == palavra[j]):
        is_palindrome = True
    else:
        is_palindrome = False
        break

    i += 1
    j -= 1

if(is_palindrome):
    print('É um palíndromo')
else:
    print('Não é um palíndromo')