nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) /2
print('sua nota foi {}'.format(media))
if media <= 5.0:
    print('sinto muito voce foi reprovado')
elif media <= 6.9 :
    print('voce esta de recuperação')
elif media >= 7:
    print('parabens voce foi aprovado <3')