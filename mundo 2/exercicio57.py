nome = input('Qual o seu nome: ')
sexo = str(input('Qual seu sexo? [M]-masculino [F]- Femino: ')).upper()
while sexo != 'F' and sexo != 'M':
    sexo = str(input('tente novamente:  ')).upper()
print(f'validação completa {nome}')
    

