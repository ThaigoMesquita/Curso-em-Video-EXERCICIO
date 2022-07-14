primaria = [],[]
for n in range(1,8):
    valor = int(input(f'digite o {n} valor: '))
    if valor % 2 == 0:
        primaria[0].append(valor)
    else:
        primaria[1].append(valor)
print(f'Os valores pares digitados foram: {primaria[0]}')
print(f'os valores impares são {primaria[1]}')
