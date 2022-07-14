'''gordo = 0
magro = 0
for c in range(1,6):
    peso = float(input(f'Qual o peso da {c} pessoa:  '))
    if peso > magro:
        print('gordinho hein')
        gordo += 1
        print(f'temos {gordo} de pessoas acima do peso')
    else:
        print('segura pro vento nao levar')
        magro +=1
        print(f'temos {magro} de pessoas abaixo do peso')'''

gordo = 0
magro = 0
for p in range(1,6):
    peso = float(input(f'Qual o peso da {p} pessoa:  '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}')
print(f'O menor peso lido foi {menor}')