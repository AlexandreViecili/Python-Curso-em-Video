# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# ex:
# 5! = 5x4x3x2x1 = 120

# Existe a função factorial() do módulo math, mas neste código farei
# manualmente e mostrando desenvolvimento.

# Usando o laço While:

n = int(input('Digite um número: '))
n2 = n - 1
print(f'{n}! = {n}', end='')
while n2 != 0:
    n = n * n2
    print(f' x {n2}', end='')
    n2 -= 1
print(f' = {n}')

# Usando o laço For:

n = int(input('Digite um número: '))
n2 = n - 1
print(f'{n}! = {n}', end='')
for i in range(n, 1, -1):
    n = n * n2
    print(f' x {n2}', end='')
    n2 -= 1
print(f' = {n}')
