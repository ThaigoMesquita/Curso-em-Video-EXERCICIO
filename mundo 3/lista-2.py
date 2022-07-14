teste = list()
teste.append('taigo')
teste.append(19)
galera = list()
galera.append(teste[:]) #copia
teste[0] = 'marisa'
teste[1] = 22
galera.append(teste[:]) #copia
print(galera)

galera = [['joao',19], ['anna',12],['joahana',14],['mariana',35]]
for p in galera:
    print(p)

totalmaior = totalmenor = 0
outra_galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: '))) 
    dado.append(int(input('Idade: ')))
    outra_galera.append(dado[:])
    dado.clear()

for p in outra_galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totalmaior+=1
    else:
        print(f'{p[0]} é menor de idade')
        totalmenor+=1
print(f'temos {totalmaior} maiores e menores temos {totalmenor}')