# Adapte o código do desafio 107, criando uma função adicional chamada moeda()
# que consiga mostrar os valores como um valor monetário formatado.

# Módulo

def metade(n=0):
    metade = n / 2
    return metade


def dobro(n=0):
    dobro = n * 2
    return dobro


def aumentar(n=0, p=0):
    aumento = n * (p / 100)
    return n + aumento


def diminuir(n=0, p=0):
    reducao = n * (p / 100)
    return n - reducao


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')

