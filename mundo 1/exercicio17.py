import math
angulo = float(input('digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangete = math.tan(math.radians(angulo))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangete))