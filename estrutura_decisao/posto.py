combustivel = input('Qual o tipo de combustível? ')
qtd_litros = input('Quantos litros?')
qtd_litros = float(qtd_litros)

total = 0
desconto = 0
if(combustivel == 'A' or combustivel == 'G'):
    if(combustivel == 'A'):
        combustivel = 'Alcool'
        total = 2.5*qtd_litros
        if(qtd_litros <= 20):
            desconto = 0.03
        else:
            desconto = 0.05

    elif(combustivel == 'G'):
        combustivel = 'Gasolina'
        total = 1.9*qtd_litros
        if(qtd_litros <= 20):
            desconto = 0.04
        else:
            desconto = 0.06
else:
    print('Opção inválida!')

desconto = total*desconto


print('Combustível: %s' % combustivel)
print('Quantidade: %gL' % qtd_litros)
print('Preço total: R$ %g' % total)
print('Desconto: R$ %g' % desconto)
print('Valor a ser pago: R$ %g' % (total-desconto))
