r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r3 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos podem formar triangulo', end='')
    if r1 == r2 and r2 == r3:
        print(' EQUILATERO')
    if r1 != r2 != r3 != r1:
        print(' ESCOLANO')
    else:
        print(' ISOSCELES')
else:
    print('os segmentos acima nao podem fomar triangulo')