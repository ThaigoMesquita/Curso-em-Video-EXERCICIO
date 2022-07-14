
#acessos a tuplas

lanche = 'hamburguer', 'suco', 'pizza', 'Pudim'
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('comi pra caramba')

# ou

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posicao {cont}')
print('comi pra caramba')
