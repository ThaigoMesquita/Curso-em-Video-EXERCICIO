lista = []
princ = list()
PesoMaior = 0
PesoMenor = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if len(princ) == 0:
        PesoMaior = PesoMenor = lista[1]
    else:
        if lista[1] > PesoMaior:
           PesoMaior = lista[1]
        if lista[1] < PesoMenor:
            PesoMenor = lista[1] 
    princ.append(lista[:])
    lista.clear()
    escolha = input('De seja continuar?[S/N]: ').strip().upper()
    if escolha == 'N':
        break
print(f'ao todo, voce cadastrou {len(princ)} pessoas')
print(f'o maior peso da lista é de {PesoMaior}kg. Peso de ',end=' ')
for p in princ:
    if p[1] == PesoMaior:
        print(f'[{p}]',end=' ')
print('')
print(f'menor peso foi {PesoMenor}',end=' ')
for p in princ:
    if p[1] == PesoMenor:
        print(f'[{p}]')