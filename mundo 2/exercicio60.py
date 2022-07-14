n = int(input('digite um numero '))
c = n
fatorial = 1
print(f'Calculando {n}!= ', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    fatorial *=c
    print('x' if c > 1 else '=', end=' ')
    c-=1
print(f'{fatorial}')

# usando for
x = int(input('digite um numero '))
m = 1
for t in range(x,0,-1):
    print(f'{t}', end='')
    if t >1:
        print('x', end=' ')
    else:
        print(' =',end=' ')
    m*=t
    t-=1
print(f'{m}')