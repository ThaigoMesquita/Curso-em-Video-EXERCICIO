expr = str(input('digite a expressao: '))
pilha = []
for simb in expr:
    if simb =='(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)> 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha)==0:
    print('sua expresao esta valida')
else:
    print('sua expresao esta errada')