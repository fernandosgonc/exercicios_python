tipo_carne = input('Qual o tipo de carne escolhido? ')
qtd_carne = float(input('E a quantidade em kg? '))
opcao_valida = True
txt_tipo_carne = ''


valor_compra = 0
preco_kg = 0
if(tipo_carne == 'F' or tipo_carne == 'f'):
    txt_tipo_carne = 'Filé Duplo'
    if(qtd_carne<=5):
        preco_kg = 4.9
    else:
        preco_kg = 5.8
elif(tipo_carne == 'A' or tipo_carne == 'a'):
    txt_tipo_carne = 'Alcatra'
    if(qtd_carne<=5):
        preco_kg = 5.9
    else:
        preco_kg = 6.8
elif(tipo_carne == 'P' or tipo_carne == 'p'):
    txt_tipo_carne = 'Picanha'
    if(qtd_carne<=5):
        preco_kg = 6.9
    else:
        preco_kg = 7.8
else:
    print('Opção inválida!')
    opcao_valida = False

if(opcao_valida):
    print('Escolha forma de pagamento: \n1 - Dinheiro \n2 - Cartão de crédito \n3 - Cartão Tabajara ')
    forma_pagamento = int(input())
    pagamento_cartao_tj = False
    txt_forma_pagamento = ''

    if(forma_pagamento == 1):
        txt_forma_pagamento = 'Dinheiro'
    elif forma_pagamento == 2:
        txt_forma_pagamento == 'Cartão de cŕedito'
    elif forma_pagamento == 3:
        txt_forma_pagamento = 'Cartão Tabajara'
        pagamento_cartao_tj = True
    else:
        print('Opção inválida!')

    valor_compra = qtd_carne*preco_kg

    desconto = 0
    if(pagamento_cartao_tj):
        desconto = (valor_compra*0.05)
        valor_compra -= desconto

    print('Você comprou %gKg de %s' %(qtd_carne, txt_tipo_carne))
    print('Você selecionou pagar utilizando %s' %txt_forma_pagamento)
    print('O valor do seu desconto é de R$ %g' %desconto)
    print('O valor a ser pago é R$ %g' %valor_compra)