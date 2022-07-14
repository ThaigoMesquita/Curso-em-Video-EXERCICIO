import random
from time import sleep

def sorteia(lista):
    for cont in range(0,5):
        n = (random.randint(1,10))
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('pronto')


def somaPar(lista):
    soma=0
    for valor in lista:
        if valor % 2 == 0:
            soma+= valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
print(numeros)
somaPar(numeros)

