'''for c in range(1,10):
    print(c)
print('fim')'''

n = 1
impa = 0
par = 0
while n != 0:
    n = int(input('digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
            ('é um numero impa')
            impa += 1
print(f'foram digitados {par} numeros pares')
print(f'foram digitados {impa} numeros impares')
print('cabou')