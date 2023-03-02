# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final
# moestre os 10 primeiro termos dessa progressão.

pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for i in range(10):
    print(f'{i+1}° termo: {pt}')
    pt = pt + r