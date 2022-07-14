distancia = float(input('Qual a distancia da viagem? '))
if distancia <= 200:
    valor = distancia * 0.50
    print('sua viagem vai custar {:.2f} R$. Tenha uma boa viagem'.format(valor))
else:
    valor_bonus = distancia * 0.45
    print('sua viagem vai custar {:.2f} R$. Tenha uma boa viagem'.format(valor_bonus))