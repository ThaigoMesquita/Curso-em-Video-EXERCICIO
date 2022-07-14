import random
v=0
while True:
   jogador = int(input('digite um numero: '))
   pc = random.randint(1,10)
   escolha = str(input('Par ou Impar[P/I]? ')).upper()[0]
   total = pc + jogador
   while escolha not in 'PI':
        escolha = str(input('Par ou Impar[P/I]? ')).upper()[0]
   print(f'voce jogou {jogador} e o computador jogou {pc}')
   if escolha == 'P':
        if total % 2 == 0:
            print('voce venceu')
            v+=1
        else:
            total % 2 == 1
            print('voce perdeu')
        break
   elif escolha == 'I':
        if total % 2 == 1:
            print('voce ganhou')
            v+=1
        else:
            total % 2 == 0
            print('voce perdeu')
            break
   print('Vamos jogar novamente')
print(f'GAME OVER!! voce venceu {v} vezes')