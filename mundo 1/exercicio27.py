nome = str(input('Qual o seu nome? '))
if nome == 'taigo':
    print('que nome estranho voce tem')
print('bom dia {}'.format(nome))


n1 = float(input('digite sua primeira nota'))
n2 = float(input('digite sua segunda nota'))
media = (n1 + n2)/2
if media >=7.0:
    print('parabens')
else:
    print('estude mais')