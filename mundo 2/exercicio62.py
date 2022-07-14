primeiro = int(input('Digite um numero: '))
razao = int(input('digite uma Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        termo = termo + razao
        print(f'{termo}', end=' ')
        cont+=1
    print('Pausa')
    mais = int(input('quantos numeros voce ainda quer ver? '))
print(f'o tatal que voce viu ate agora foi {total}')








"""primeiro = int(input('Digite um numero: '))
razao = int(input('digite uma Razão'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        termo = termo + razao
        print(f'{termo}', end=' ')
        cont+=1
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print(f'progressa finalizada com {total} termos')"""