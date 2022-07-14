a = int(input('digite um numero: '))
b = int(input('digite um segundo numero: '))
c = int(input('digite um terceiro numero: '))
menor = a 
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('menor valor foi {}'.format(menor))
#verificando maior
maior = a 
if b > a and b > c:
    maior = b
if c > a and c > a:
    maior = c
print('o maior valor foi {}'.format(maior))