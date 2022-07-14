import math
co = float(input('Entre com o valor do cateto oposto: '))
ca = float(input('Entre com o valor do cateto adjacente: '))
hi = (co ** 2 + ca **2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))


# com hiportação
co2 = float(input('Entre com o valor do cateto oposto: '))
ca2 = float(input('Entre com o valor do cateto adjacente: '))
hi2 = math.hypot(co2, ca2)
print('A hipotenusa vai medir {:.2f}'.format(hi2))