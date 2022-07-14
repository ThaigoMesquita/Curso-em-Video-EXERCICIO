valores = list()
menor = 0
maior = 0
for c in range(0,5):
    valores.append(int(input('digite um numero: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
for n, v in enumerate(valores):
    if v == maior:
        print(f'o maior valor foi {maior} e esta na posicao {n}')  
    elif v == menor:
        print(f'o menor valor foi {menor} e esta na posicao {n}')  

