lista = []
pares = []
impares = []
while True:
    numero = int(input('digite um numero: '))
    lista.append(numero)
    escolha = input('Quer continuar[S/N] ').upper().strip()
    if numero % 2 == 0:
        pares.append(numero)
    if numero % 2 == 1:
        impares.append(numero)
    if escolha == 'N':
        break
print(f'a lista completa é {lista}')
print(f'a lista de numeros pares é {pares}')
print(f'a lista de numeros impares é de {impares}')