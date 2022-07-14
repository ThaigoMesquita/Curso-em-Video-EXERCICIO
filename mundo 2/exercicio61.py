primeiro = int(input('Digite um numero: '))
razao = int(input('digite uma Razão'))
termo = primeiro
cont = 1
while cont <=10:
    termo = termo + razao
    print(f'{termo}', end=' ')
    cont+=1
print('fim')