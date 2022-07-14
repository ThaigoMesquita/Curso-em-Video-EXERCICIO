import random
lista = list()
tot = 1
jogos = list()
print('-'*30)
print('     JOGAR NA MEGA SENA      ')
print('-'*30)
escolha = int(input('Quantos jogos voce quer que eu sortei? '))
while tot <= escolha:
    cont=0
    while True:
        num = random.randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print('-='*3, f' Sorteando {escolha} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')