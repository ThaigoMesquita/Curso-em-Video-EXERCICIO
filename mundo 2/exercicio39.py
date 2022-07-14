nascimento = int(input('Ano de nascimento: '))
idade = 2022 - nascimento 
alistamento = idade - 18
print('voce nasceu em {} e tem {} anos'.format(nascimento,idade))
if idade == 18:
    print('se aliste imediatamente')
elif idade < 18:
    print('voce nao tem 18 anos ainda')
    print('ainda falta {} anos para o alistamento'.format(18 - idade))
    print('seu alistamento sera{}'.format())
elif idade > 18:
    print('voce ja deveria ter se alistado há {}'.format(idade - 18))
    print('seu alistamento foi em {}'.format(2022 - alistamento ))
