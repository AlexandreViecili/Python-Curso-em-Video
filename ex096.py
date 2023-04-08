# Faça um programa que tenha uma função chamada área(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def área(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg:.1f}x{comp:.1f} é de {area:.1f}m².')


#Programa Principal
print('  Controle de Terrenos  ')
print('-' * 24)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura, comprimento)