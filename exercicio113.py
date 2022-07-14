def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('DIGITE UM NUMERO REAL VALIDO')
            continue
        except (KeyboardInterrupt):
            print('O USUARIO NAO DIGITOU NENHUM VALOR')
            return 0
        else:
            return msg


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('DIGITE UM NUMERO REAL VALIDO')
            continue
        except (KeyboardInterrupt):
            print('O USUARIO NAO DIGITOU NENHUM VALOR')
            return 0
        else:
            return msg
        


        
n1 = leiaInt('digite um inteiro: ')
n2 = leiaFloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real foi {n2}')
 

