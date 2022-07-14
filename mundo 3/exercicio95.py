def area(larg, comp):
    a = larg * comp
    print(f' a area de um terreno {larg}x{comp} é de {a}')

#Programa principal
print('Controle de Terrenos')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l,c)