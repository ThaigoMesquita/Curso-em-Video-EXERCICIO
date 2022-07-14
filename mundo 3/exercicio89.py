boletim = list()
escola = {'nome':str(input('Nome: ')), 'media':int(input('Media: '))}
boletim.append(escola.copy())
print('-='*10)
for e in boletim:
    for k, v in e.items():
        print(f'O {k} é igual a {v}')               # eu
for v in escola:
    if escola['media'] >= 70:
        print('situação é igual a aprovado')
        break
    if escola['media'] > 60:
        print('situação em igual recuperação')
        break
    else: 
        print('reprovado')
        break


aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno ['situação'] = 'Aprovado'
elif 5 <=['media'] < 7:
    aluno ['situação'] = 'Recuperação'
else:
    aluno ['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'O {k} é igual a {v}')