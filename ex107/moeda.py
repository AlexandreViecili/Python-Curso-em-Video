# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

# Módulo

def metade(n):
    metade = n / 2
    return metade


def dobro(n):
    dobro = n * 2
    return dobro


def aumentar(n, p):
    aumento = n * (p / 100)
    return n + aumento


def diminuir(n, p):
    reducao = n * (p / 100)
    return n - reducao

