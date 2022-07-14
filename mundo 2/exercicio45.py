import random
from time import sleep
itens = ('Pedra', 'Papel' , 'Tesoura')
print("""suas opções:
[0] Pedra
[1] Papel
[2] Tesoura""")
pc = random.randint(0, 2)
jogador = int(input('Qual é a sua Jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!!!')
print('-=' * 11)
print('computador jogou {}'.format(itens[pc]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if pc == 0: #computador jogou PEDRA
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif pc == 1: #computador escolheu PAPEL
    if jogador == 1:
        print('empate')
    elif jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif pc == 2: # computador escolheu tesoura
    if jogador == 2:
        print('empate')
    elif jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')