from datetime import date
atual = date.today().year
nascimento = int(input('Qual a sua idade? '))
idade = atual - nascimento
print('sua idade é {}'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
     print('Classificação: INFANTIL')
elif idade <= 18:
     print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')