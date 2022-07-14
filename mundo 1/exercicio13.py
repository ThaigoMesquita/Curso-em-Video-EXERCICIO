dias = int(input('digite por quantos dias voce alugou o carro?: '))
km = int(input('quantos km voce pecorreu?: '))
pago = dias * 60 + (km * 0.15)
print('o total que voce tem que pagar é: {:.2f}'.format(pago))  