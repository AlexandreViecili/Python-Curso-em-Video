# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n1 = int(input('Digite um número para ver sua tabuada: '))
print('-' * 15)
for i in range(10):
    print(f'{i+1} x {n1} = {(i+1)*n1}')
print('-' * 15)
