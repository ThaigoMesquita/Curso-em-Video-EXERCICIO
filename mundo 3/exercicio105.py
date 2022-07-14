def nota (*ns, sit=False):
    """
    -> Função que mostra uma situação geral de notas dos alunos:
    :param qtdnt: quantidade de notas inseridas;
    :param maiorn: maior nota inserida;
    :param menorn: menor nota inserida;
    :param median: média das notas inseridas;
    :param sit: situação dos alunos;
    :return: retorna todos os parametros acima dentro ou não de uma situação
    """
    notas = dict()
    notas['total'] = len(ns)
    notas['maior'] = max(ns)
    notas['menor'] = min(ns)
    notas['media'] = round(sum(ns) / len(ns))
    if sit:
        if notas['media']>=7:
            notas['situação'] = 'BOA'
        if notas['media']>=5:
            notas['situação'] = 'RAZOAVEL'
        else:
            notas['situação'] = 'SITUAÇÃO MUITO RUIM'
    return notas

#Programa principal
boletim = nota(5.5, 5,7,5,sit=True) 
print(boletim)
help(nota)





