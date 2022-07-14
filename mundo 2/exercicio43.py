peso = int(input('Qual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura * altura)
print('seu imc é {:.1f}'.format(imc))
if imc <= 18.5:
    print('voce esta abaixo do normal')
elif  18.5 <= imc < 25:
    print('Normal')
elif 25.0 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc > 40:
    print('obesidade morbida')