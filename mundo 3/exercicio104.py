def leiaInt(msg):
    while True:
        print('-='*10)
        n = str(input(msg))
        if n.isnumeric():
            print(f'Voce acabou de digitar o numero {n}')
            break
        else:
            print('ERRO')
        

n = leiaInt('digite um numero: ')

