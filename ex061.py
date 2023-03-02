# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
# os 10 primeiros termos da progressão usando a estrutura while.

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termos = 1
while termos != 11:
    print(f'{termos}° termo: {pt}')
    pt = pt + r
    termos += 1