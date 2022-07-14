from datetime import date
atual = date.today().year
totalMaior = 0
totalMenor = 0
for pess in range(1,8):
    nasc = int(input(f'Em que ano a pessoa {pess} nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        print('essa pessoa é maior')
        totalMaior += 1
    else:
        print('essa pessoa é menor')
        totalMenor += 1
print(f'ao todo tivemos {totalMaior} pessoas maiores de idade')
print(f'ao todo tivemos {totalMenor} pessoas menores de idade')


"""for c in range(1,8):
    pessoas = int(input(f'Em que ano a {c} nasceu? '))
    if pessoas > 18:
        print(f'temos {c} maior de idade')
    elif pessoas < 18:
        print(f'temos {c} menor de idade')"""