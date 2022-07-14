numero = int(input('insira um nuemro para ver a tabuada: '))
print('---------------')
print('{} x {} = {}'.format(numero,1,numero*1))
print('{} x {} = {}'.format(numero,2,numero*2))
print('{} x {} = {}'.format(numero,3,numero*3))
print('{} x {} = {}'.format(numero,4,numero*4))
print('{} x {} = {}'.format(numero,5,numero*5))
print('{} x {} = {}'.format(numero,6,numero*6))
print('{} x {} = {}'.format(numero,8,numero*8))
print('{} x {} = {}'.format(numero,9,numero*9))
print('{} x {} = {}'.format(numero,10,numero*10))
print('---------------')


# ou

number = int(input('Escolha um numbero para a tabuada: '))
number2 = 0

print('-' * 14)
print('A tabuada de {} é:'.format(number))

while (number2 <= 10):
    print('{} x {} = {}'.format(number2, number,(number2 * number)))
  
    number2 = number2 + 1
print('-' * 14)   
