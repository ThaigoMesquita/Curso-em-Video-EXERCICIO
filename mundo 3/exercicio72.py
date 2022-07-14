numero = 'zero','um', 'dois', 'tres', 'quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'
while True:
    n = int(input('digite um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'voce digitou {numero[n]}')
    else:
        print('numero invalido')
    escolha = input('Deseja tentar novamente? [S/N] ').strip().upper()
    if escolha == 'N':
        break
    while escolha != 'N':
        if escolha == 'S':
         n = int(input('digite um numero entre 0 e 20: '))
        if 0 <= n <= 20:
            print(f'voce digitou {numero[n]}')
        else:
            print('numero invalido')
        escolha = input('Deseja tentar novamente? [S/N] ').strip().upper()
    if escolha == 'N':
        break