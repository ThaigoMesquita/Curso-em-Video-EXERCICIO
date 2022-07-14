maior_de_idade = 0
mulheres = 0
homens = 0
while True:
    print('-'*10)
    print('CADASTRE UMA PESSOA')
    print('-'*10)
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo:[M/F] ').strip().upper()[0]
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('quer continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        maior_de_idade+=1
    if sexo == 'm':
        homens+=1
    if idade < 20 and sexo == 'f':
            mulheres+=1
    if escolha == 'N':
        break
print(f'na lista temos {homens} homens cadastrados')
print(f'temos {maior_de_idade} pessoas maiores de idade')
print(f'e temos {mulheres} mulheres com menos de 20')
    

