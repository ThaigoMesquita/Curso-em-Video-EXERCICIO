imovel = float(input('valor da casa: '))
salario = float(input('salario do comprador: '))
anos = int(input('quantos anos voce vai pagar? '))
prestacao = imovel /(anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(imovel, anos))
print('a prestação sera de {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('CONCEDIDO')
else:
    print('negado')