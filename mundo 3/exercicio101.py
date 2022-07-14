def voto(ano):
   from datetime import date
   hoje = date.today().year
   idade = hoje - ano
   if hoje - ano >= 18 and hoje - ano < 70:
        return f'com {idade} o voto é obrigatorio'
   elif hoje - ano  >= 16:
        return f'com {idade} o voto é opcional'
   else:
        return f'com {idade} ainda não pode votar'
    

ano_nascimento = int(input('Em qual ano voce nasceu: '))
print(voto(ano_nascimento))




    

