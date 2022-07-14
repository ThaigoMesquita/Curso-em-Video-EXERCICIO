def jogador(nome = 'desconhecido', gols = 0):
    if gols.isnumeric():
        gols = int(gols)
    if nome == '':
        nome = "desconhecido"
    if gols =='':
        gols = '0'
    return f'jogador {nome} fez {gols} na copa do mundo'
      

nome = str(input('Nome do jogador: '))
gols = str(input('quantos gols?: '))
print(jogador(nome, gols))

