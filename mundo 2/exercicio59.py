from time import sleep
numero = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
sair = False
while sair != True:
    print('-' *10)
    print("""
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa""")
    print('-' *10)
    escolha = int(input('qual é a sua opção? '))  
    if escolha == 1:
        soma = numero + numero2
        print('calculando...')
        sleep(1)
        print(f'resultado é {soma}')
    elif escolha == 2:
        multiplicar = numero * numero2
        print('calculando...')
        sleep(1)
        print(f'A multipliação entre {numero} e {numero2} é {multiplicar}')
    elif escolha == 3:
        if numero > numero2:
            print('calculando...')
            sleep(1)
            print(f'numero {numero} é maior que {numero2}')
        else:
            print('calculando...')
            sleep(1)
            print(f'numero {numero2} é maior que {numero}')
    elif escolha == 4:
        print('infrome novos numeros')
        numero = int(input('Digite um numero: '))
        numero2 = int(input('Digite um numero: '))
    elif escolha == 5:
        sair = True

