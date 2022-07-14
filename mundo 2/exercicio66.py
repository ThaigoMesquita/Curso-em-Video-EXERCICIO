numero = int(input('digite um valor (999 para parar): '))
soma = numero
total = 0
while numero != 999:
    numero = int(input('digite um valor (999 para parar): '))
    total+=1
    if numero == 999:
        break
    soma+=numero
print(f'a soma {total} é de {soma}')
