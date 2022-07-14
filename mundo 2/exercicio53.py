frase =str(input('digite uma frase: ')).strip().upper()
palavra = frase.split()
junto =  ''.join(palavra)
inverso = ''
print(f'voce digitou a frase {palavra}')
for letra in range(len(junto) -1,-1,-1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print(f'temos um palidromo')
else:
    print(f'nao é palidromo')

    # ou
frase =str(input('digite uma frase: ')).strip().upper()
palavra = frase.split()
junto =  ''.join(palavra)
inverso = junto [::-1]
print(f'voce digitou a frase {palavra}')
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print(f'temos um palidromo')
else:
    print(f'nao é palidromo')