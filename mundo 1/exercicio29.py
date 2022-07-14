velocidade = float(input('Qual era a sua velocidade? '))
if velocidade <= 80:
    print('muito bem. continue nessa velocidade{}'.format(velocidade))
elif velocidade > 80:
    multa = (velocidade-80) * 7
    print('ULTRAPASSOU A VELOCIDADE 80km')
    print('VOCE TERA A MULTA DE {:.2f}'.format(multa))
print('tenha um bom dia! Dirija com segurança')
    