palavra = "aprender", 'programar', 'linguagem','python','curso','gratis', 'estudar'
for p in palavra:
    print(f'na palavra {p} temos')
    for letra in p: 
        if letra.lower() in 'aeiou':
            print(letra, end ='   ')