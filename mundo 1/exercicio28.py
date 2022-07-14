import random
from time import sleep
print('-=-' *20)
print('Vou pensar em um numero entre 0 e 5. tente acertar')
print('-=-' *20)
numero = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
computador = random.randint(0, 5)
if numero == computador:
    print('ohhh parabens voce acertou')
    print('o numero escolhido do pc foi {}'.format(computador))
else:
    print('tente novamente')
    print('o numero escolhido do pc foi {}'.format(computador))









