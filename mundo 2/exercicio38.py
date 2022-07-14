numero1 = int(input('Primeiro Numero: '))
numero2 = int(input('Segundo Numero: '))
if numero1 > numero2:
    print('o numero {} é maior'.format(numero1))
elif numero2 > numero1:
    print('o numero {} é maior'.format(numero2))
elif numero2 == numero1:
    print('ambos sao iguais')