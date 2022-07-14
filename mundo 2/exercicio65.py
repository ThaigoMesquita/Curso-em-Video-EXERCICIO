total = 0
fim = False
soma = 0
maior = 0
menor = 9999999999999999999999999
while fim != True:
    numero = int(input('digite um numero: '))
    total +=1
    soma +=numero
    media = soma / 4
    if numero > maior:
        maior = numero
    if  numero < menor:
        menor = numero
    escolha = input('Deseja continuar [s/n] ')
    if escolha == 'n':
        fim == True
        break  
print(f'A media de {total} foi de {media} ')
print(f'O maior numero foi {maior} e o menor foi {menor}')