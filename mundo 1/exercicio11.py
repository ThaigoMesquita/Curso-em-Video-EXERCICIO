salario = float(input('quanto o funcionario recebe? R$:'))
aumento = salario + (salario  * 15 / 100)
print('o funcionario que tinha o salario de R${} teve o aumento de R${:.2f}'.format(salario, aumento))