# Faça um programa que leia a largura e a altura de uma parede em metros, calcule
# a sua área e a quantidade de tinta necessária para pintá-lo, sabendo que cada
# litro de tinta pinta uma área de 2m².

l = float(input('Dê a largura em metros: '))
a = float(input('Dê a altura em metros: '))
area = l * a
tinta = area / 2
print(f'A área é de {area}m² e precisa de {tinta} litros de tinta.')
