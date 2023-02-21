#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente 
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

catOp = float(input('Digite o comprimento do cateto oposto: '))
catAdj = float(input('Digite o comprimento do catetro adjacente: '))
hipotenusa = hypot(catOp, catAdj)
print(f'A hipotenusa é {hipotenusa:.2f}.')
