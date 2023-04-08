# Adcione ao módulo moeda.py criado nos desafios anteriores, uma função chamada
# resumo(), que mostre na tela algumas informações geradas pelas funções que já
# temos no módulo criado até aqui.

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
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n, a, r):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado:     {moeda(n)}')
    print(f'Dobro do preço:      {dobro(n, True)}')
    print(f'Metade do preço:     {metade(n, True)}')
    print(f'{a}% de aumento:      {aumentar(n, a, True)}')
    print(f'{r}% de redução:      {diminuir(n, r, True)}')
    print('-' * 30)