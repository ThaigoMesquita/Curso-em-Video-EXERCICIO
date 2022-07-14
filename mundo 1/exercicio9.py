largura = float(input('largura da parede: '))
altura = float(input('altura da parede: '))
area_total = largura * altura
litro =  area_total /2
print('sua parede tem a dimensao de {}x{} e sua área total é de {}, sera preciso {} litros para pintar sua parede'.format(largura,altura,area_total, litro))