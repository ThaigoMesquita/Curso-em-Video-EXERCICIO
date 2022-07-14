lista = list()
numero=(int(input('Digite um valor: ')))
escolha = input('Quer continuar[S/N] ').strip().upper()
lista.append(numero)
while True:
    numero=(int(input('Digite um valor: ')))
    if numero in lista:
        print('ESTE VALOR CONTÉM NA LISTA')
        continue
    if numero != lista:
        lista.append(numero)
    escolha = input('Quer continuar[S/N] ').strip().upper()
    if escolha in 'Nn':
        break
lista.sort()
print(f'{lista}')