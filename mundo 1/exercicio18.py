import random
nome1 = input('digite o nome do primeiro aluno: ')
nome2 = input('digite o nome do segundo aluno: ')
nome3 = input('digite o nome do terceiro aluno: ')
nome3 = input('digite o nome do quarto aluno: ')
lista = [nome1,nome2,nome3]
escolhido = random.choice(lista)
print('quem foi escolhido foi: {}'.format(escolhido))