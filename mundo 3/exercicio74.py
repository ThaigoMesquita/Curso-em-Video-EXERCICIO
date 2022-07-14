import random
maior = 0
menor = 999999999999999999999
tupla = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))
for c in tupla:
    if  c > maior:
        maior = c
    if c < menor:
        menor = c
print(tupla)
print(f'o maior numero {maior}')
print(f'o menor numero foi {menor}')


