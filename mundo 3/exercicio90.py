import enum
import random
from time import sleep
from operator  import itemgetter
jogador = dict()
jogador['jogador1'] = random.randint(1,6)
jogador['jogador2'] = random.randint(1,6)
jogador['jogador3'] = random.randint(1,6)
jogador['jogador4'] = random.randint(1,6)
raking=list()
print('Valores sorteados: ')
for k, v in jogador.items():
    print(f'o jogador {k} jogou o dado {v}')
    sleep(1)
raking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(raking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')