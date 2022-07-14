print('caso queria sair digite 999: ')
numero = int(input('digite um numero: '))
total = 0
soma = numero
while numero != 999:
    if numero == 999:
      break
    numero = int(input('digite um numero: '))
    if numero != 999:
      total+=1
      soma += numero 
print(f'voce acumulou {soma}')  
  



