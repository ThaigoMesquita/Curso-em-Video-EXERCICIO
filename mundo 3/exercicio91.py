cadastro = dict()
cadastro['Nome'] = str(input('Nome: '))
cadastro['idade'] = int(input('Ano de nascimento: '))
cadastro['idade'] = 2022 - cadastro['idade']
cadastro['CTPS'] = int(input('Carteira de Trabalho ( digite 0 caso nao tenha):  '))
if cadastro['CTPS'] == 0:
    print('-='*20)
    for k, v in cadastro.items():
        print(f'{k} tem o valor de {v}')
else:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['aposentadoria'] = (cadastro['Contratação'] + 35) - 2022
    cadastro['salario'] = int(input('Salario: '))
    print('-='*20)
    for k, v in cadastro.items():
        print(f'{k} tem o valor de:  {v}')