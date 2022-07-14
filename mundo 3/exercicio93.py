cadastro = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [F/M]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    cadastro.append(pessoa.copy())
    while True:
      escolha = input('Quer continuar? [S/N]').upper()[0]
      if escolha in 'SN':
          break
      print('ERRO, RESPONDA APENAS S OU N').upper()[0]
    if escolha in 'N':
            break
print('-='*30)
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas')
media = soma/len(cadastro)     
print(f'B) A media de idade é de {media:5.2f} anos')
print(f'C) as mulheres cadastradas foram', end=' ')
for p in cadastro:
    if p['sexo'] in 'Ff':
        print(f'{ p["nome"]} ', end='')
print()
print('D) LISTA DE PESSOAS A CIMA DA MEDIA:', end=' ')
for p in cadastro:
    if p['idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v}:', end='')
        print()
print('encerrado')