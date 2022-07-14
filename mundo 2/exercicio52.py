num = int(input('digite um numero: '))
contador = 0
for n in range(1,num + 1):
    if num % n == 0:
        contador += 1
print('o numero {} foi divisivel {}'.format(num, contador))
if contador == 2:
    print('o numero é primo')
else:
    print('o numero nao é primo')
