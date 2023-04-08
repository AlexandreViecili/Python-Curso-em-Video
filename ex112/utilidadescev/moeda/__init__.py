# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo
# chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de
# funcionar como a função input(), mas com uma validação de dados para aceitar
# apenas valores que sejam monetários.

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