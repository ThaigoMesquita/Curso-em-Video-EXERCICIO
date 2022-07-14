while True:
    tabuada = int(input('qual o numero que voce quer ver a tabuada? '))
    if tabuada < 0:
       break
    print('-' *12)
    for c in range(1,10):
        print(f'{tabuada} x {c} = {tabuada*c}') 
    print('-' *12)
print('numero invalido') 
