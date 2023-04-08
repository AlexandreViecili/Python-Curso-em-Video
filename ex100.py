# Faça um programa que tenha uma lista chamada números e duas funções chamadas
# sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
# dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# PARES sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia():
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        n = randint(1, 10)
        lista.append(n)
        print(n, end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')

lista = []

def somaPar(n):
    total = 0
    for n in lista:
        if n % 2 == 0:
            total += n
    print(f'Somando os valores pares de {lista}, temos {total}.')

sorteia()
somaPar(lista)