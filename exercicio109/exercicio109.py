import moeda

preco = float(input('Digite um valor: '))
print('-='*10)
print(f'metade do valor de {moeda.moeda(preco)} é de {moeda.metade(preco, True)}')
print(f'o dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'aumentando 10%, temos é {moeda.aumentar(preco,10, True)}: ')
print(f'Reduzindo 13%, temos {moeda.diminuir(preco,13,True)}')
print('-='*10)



