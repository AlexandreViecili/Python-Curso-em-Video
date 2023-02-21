# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

cores = {'limpa':'\033[m','amarelo':'\033[0;33m','verde':'\033[0;32m','vermelho':'\033[0;31m'}
n1 = int(input(f'{cores["amarelo"]}Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'{cores["verde"]}O número {n1} é o maior.{cores["limpa"]}')
if n2 > n1 and n2 > n3:
    print(f'{cores["verde"]}O número {n2} é o maior.{cores["limpa"]}')
if n3 > n1 and n3 > n2:
    print(f'{cores["verde"]}O número {n3} é o maior.{cores["limpa"]}')

if n1 < n2 and n1 < n3:
    print(f'{cores["vermelho"]}O número {n1} é o menor.{cores["limpa"]}')
if n2 < n1 and n2 < n3:
    print(f'{cores["vermelho"]}O número {n2} é o menor.{cores["limpa"]}')
if n3 < n1 and n3 < n2:
    print(f'{cores["vermelho"]}O número {n3} é o menor.{cores["limpa"]}')
