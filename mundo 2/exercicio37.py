numero = int(input('digite um numero inteiro: '))
print('''Escolha uma das bases para a conversão:
[1] converter para BINARIO
[2] converter para OCTAL
[3] convereter para HEXADECIMAL''')
escolha = int(input('Faça sua escolha: '))
if escolha == 1:
    binario = format(numero, "b")
    print('transformando {} em binario fica {}'.format(numero, binario))
elif escolha == 2:
    octal = format(numero, 'o')
    print('transformando {} em binario fica {}'.format(numero, octal))
elif escolha == 3:
    hexa = format(numero, 'x')
    print('transformando {} em binario fica {}'.format(numero, hexa))
else:
    print('opção invalida')