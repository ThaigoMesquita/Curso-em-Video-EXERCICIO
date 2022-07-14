import enum


time = list()
jogador = dict()
partida = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partida.clear()
    for c in range(0,total):
        partida.append(int(input(f' Quantos gols na partida {c}?')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! RESPONSA APENAS S OU N')
    if resp == 'N':
            break
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para encerrar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! NAO EXISTE JOGADOR COM O CODIGO{busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGAFOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    no jogo {i+1} fez {g} gols')
    print('-' * 40)
print('-- volte sempre --w')
