# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

from math import cos, sin, tan, radians

ang = float(input('Digite um ângulo: '))
coss = cos(radians(ang))
seno = sin(radians(ang))
tang = tan(radians(ang))
print(f'O ângulo de {ang}º possui: ')
print(f'Seno: {seno:.2f}')
print(f'Cosseno: {coss:.2f}')
print(f'Tangente: {tang:.2f}')