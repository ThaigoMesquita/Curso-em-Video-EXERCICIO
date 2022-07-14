def metade (valor=0, formato = False):
    resp = valor /2
    return resp  if formato is False else moeda(resp)

def aumentar (valor=0, porcentual=0, formato= False):
    resp = valor + (valor * porcentual / 100)
    return resp  if formato is False else moeda(resp)

def diminuir (valor=0, porcentual=0, formato = False):
    resp = valor - (valor * porcentual / 100)
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