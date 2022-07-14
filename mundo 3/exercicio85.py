matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor na posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]               
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
print('••' * 14)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^15}]', end='')
    print()
print('••' * 14)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da terceira linha é {maior}')