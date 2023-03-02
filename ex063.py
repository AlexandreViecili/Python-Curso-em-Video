# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n
# primeiros elementos de uma Sequência de Fibonacci.
# Ex:
# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

elementos = int(
    input('Digite quantos elementos da Sequência de FIbonnaci você quer ver: '))
n1 = 0
n2 = 1
print(f'{n1} -> {n2}', end='')
c = 3
while c <= elementos:
    n3 = n1 + n2
    print(f' -> {n3}', end='')
    n1 = n2
    n2 = n3
    c += 1
