salario = float(input('Digite o valor do salario: '))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
if salario <= 1250:
    aumento = salario + (salario * 15 / 100 )
print('O seu salario é de {:.2f} e voce tera um aumento de R${:.2f}'.format(salario,aumento))