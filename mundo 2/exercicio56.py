media = 0
somaidade = 0
MaioridadeHomem = 0
nomeH = 0
totalMulher = 0

for pess in range(1,5):
    print(f'-----{pess}-----')
    nome = input('nome: ')
    idade = int(input('idade: '))
    sexo = input('Sexo [M/F]: ').upper()
    somaidade += idade
    media = somaidade / 4
    if pess == 1 and sexo in 'Mm':
        MaioridadeHomem = idade
        nomeH = nome
    if sexo in 'Mm' and idade > MaioridadeHomem:
        MaioridadeHomem = idade
        nomeH = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher+=1

print(f'o homem com mais idade é {nomeH} e tem {MaioridadeHomem} anos')
print(f'A soma de todas as idades é: {media}')
print(f' a quantidade de mulheres abaixo dos 20 é {totalMulher}')

