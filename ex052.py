# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))

primo = 0

for i in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end='')
        primo += 1
    else:
        print('\033[31m', end='')
    print(f'{i} ', end='')
print(f'\033[m\nO número {n} foi divisível {primo} vezes')
if primo == 2:
    print('Por isso ele É primo.')
else:
    print('Por isso ele NÃO é primo')