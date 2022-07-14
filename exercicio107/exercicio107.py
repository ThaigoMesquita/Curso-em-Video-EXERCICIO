import moeda
preco = int(input('Digite um valor: '))
print('-='*10)
print(f'metade do valor de {preco} é de {moeda.metade(preco)}')
print(f'o dobro de {preco} é R${moeda.dobro(preco)}')
print(f'aumentando 10%, temos é R${moeda.aumentar(preco,10)}: ')
print('-='*10)


