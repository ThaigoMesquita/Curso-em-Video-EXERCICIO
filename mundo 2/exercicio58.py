import random
print('Sou seu computador..')
print('Acabei pensar em um numero de 0 a 10')
numero = int(input('em que numero pensei? '))
tentativas = 0
acertou = False
pc = random.randint(0,10)
while not acertou:
    if numero == pc:
        print('acertou')
        acertou = True
    else: 
            if numero < pc:
                print('mais um pouco, esta perto')
            elif numero > pc:
                print('que isso mestre, é menos')
    tentativas +=1
    if numero != pc:
        numero = int(input('tenta novamente? '))
print(f'voce tentou {tentativas}')