def pega_teclado(msg):
    retorno = float(input(msg))
    return retorno

area_pintura = pega_teclado('Qual a área em metros² a ser pintada?')
area_pintura = area_pintura+(area_pintura*0.1)

cobertura_lata = 18*6
cobertura_galao = 3.6*6

qtd_latas = area_pintura//cobertura_lata+1
qtd_galoes = area_pintura//cobertura_galao+1

parcial_latas = area_pintura//cobertura_lata
area_parcial_galoes = area_pintura%cobertura_lata
parcial_galoes = area_parcial_galoes//cobertura_galao+1

print("parcial latas %d, preco: %g" %(parcial_latas, (parcial_latas*80)))
print("parcial galoes %d, preco: %g" %(parcial_galoes, (parcial_galoes*25)))


preco_latas = qtd_latas*80
preco_galoes = qtd_galoes*25
preco_mix = (parcial_latas*80) + (parcial_galoes*25)
print('Unicamete latas:  %d latas, total R$%g' %(qtd_latas, preco_latas))
print('Unicamete galoes:  %d galoes, total R$%g' %(qtd_galoes, preco_galoes))
print('Mix:  %d latas e %d galoes, total R$%g' % (parcial_latas, parcial_galoes, preco_mix))
