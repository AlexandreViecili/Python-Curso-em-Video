# Modifique as funções que foram criadas no desafio 107 para que elas aceitem
# um parâmetro a mais, informando se o valor retornado por elas vai ser ou não
# formatado pela função moeda(), desenvolvida no desafio 108.

# Módulo

def metade(n=0, format=False):
    metade = n / 2
    if format:
        return moeda(metade)
    return metade


def dobro(n=0, format=False):
    dobro = n * 2
    if format:
        return moeda(dobro)
    return dobro


def aumentar(n=0, p=0, format=False):
    aumento = n * (p / 100)
    if format:
        return moeda(n + aumento)
    return n + aumento


def diminuir(n=0, p=0, format=False):
    reducao = n * (p / 100)
    if format:
        return moeda(n - reducao)
    return n - reducao


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')

