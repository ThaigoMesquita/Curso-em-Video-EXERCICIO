num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print('Nao achei o numero 5')
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(6)
valores.append(7)
valores.append(8)
for c, v in enumerate(valores):
    print(f'na posicao {c} encontrei o valor {v}...')
print('fim')

# ler valores pelo teclado e colocar na lista
valor = list()
for cont in range(0,5):
    valor.append(int(input('digite um valor: ')))
