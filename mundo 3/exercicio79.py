lista = []
total = 0
while True:
    numero = int(input('digite um valor: '))
    lista.append(numero)
    escolha = input('Quer Continuar[S/N]? ').strip().upper()
    total+=1
    if escolha == 'N':
     break
lista.sort(reverse=True)
print(f'o total de numeros adicionados foram {total} elementos')
print(f'Os valores em ordem decresentes são {lista}')
if 5 in lista:
    print('o 5 se encontra na lista')
else:
    print('o 5 nao se encontra na lista')



