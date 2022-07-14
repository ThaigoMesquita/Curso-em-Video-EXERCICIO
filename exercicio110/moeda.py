def metade (valor=0, formato = False):
    resp = valor /2
    return resp  if formato is False else moeda(resp)

def aumentar (valor=0, porcentual=0, formato= False):
    resp = valor + (valor * porcentual / 100)
    return resp  if formato is False else moeda(resp)

def diminuir (valor=0, taxa=0, formato = False):
    resp = valor - (valor * taxa / 100)
    return resp  if formato is False else moeda(resp)

def dobro (valor=0, formato=False):
    resp = valor *2
    return resp  if formato is False else moeda(resp)
   
def moeda(preco=0,moeda = 'R$'):
    """
    Essa função mostra um valor configurado de modo monetário(com cifrão, vírqula...)
    :param n: É o valor que será formatado
    :return: string formatada
    """
    return f'{moeda}{preco:>.2f}'.replace('.',',')


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada =='': 
            print(f'ERRO {entrada} é invalido')
        else:
            valido = True
            return float(entrada)
    


def resumo(preco=0, taxa=5, porcentual = 10 ):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado:    {moeda(preco)}')
    print(f'O dobro do preço:   {dobro(preco, True)}')
    print(f'Metade do preço:    {metade(preco,True)}')
    print(f'{porcentual} de aumento:     {aumentar(preco, porcentual, True)}')
    print(f'{taxa} de redução:     {diminuir(preco, taxa, True)}')
    print('-'*30)