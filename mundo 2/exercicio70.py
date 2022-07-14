total = 0
menor = 0
cont = 0
topMil = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    cont+=1
    total += preco
    if preco > 1000:
        topMil+=1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    escolha = input('Quer Continuar comprando?[S/N]: ' ).strip().upper()
    if escolha == 'N':
        break
print(f'o total de compras foi {total}')
print(f'foram {topMil} compras acima de 1000')
print(f'o produto mais barato custa R$ {menor} e é um {barato} ')

    
total = 0
totMil = 0
menor = 0
cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preco:R$ '))
    cont +=1
    total += preco
    if preco >= 1000:
        totMil+=1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar?[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('fim do programa')
print(f'o valor total das compras foi R${total}')
print(f'temos {totMil} produtos custando mais de R$ 1000 reais')
print(f'o produto mais barato custa R$ {menor} e é um {barato} ')
