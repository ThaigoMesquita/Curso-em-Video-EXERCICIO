nome = input('Digite uma frase: ').upper().strip()
print('a letra A aparece {}'.format(nome.count('A')))
print('a letra A aparece primeiro em {}'.format(nome.index('A')))
print('a letra A aparece pela ultima vez {}'.format(nome.rfind('A')))