# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma
# lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = []
temp = []

mais = menos = 0
escolha = ''
while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso em Kg: ')))
    if len(lista) == 0:    
        mais = menos = temp[1]
    else:
        if temp[1] > mais:
            mais = temp[1]
        if temp[1] < menos:
            menos = temp[1]
    lista.append(temp[:])
    temp.clear()
    escolha = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Opção inválida.')
        escolha = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break

print(f'{len(lista)} pessoas foram cadastradas.')
print(f'O maior peso foi de {mais}Kg. Peso de ', end='')
for c in lista:
    if c[1] == mais:
        print(f'[{c[0]}] ', end='')
print(f'\nO menor peso foi de {menos}Kg. Peso de ', end='')
for c in lista:
    if c[1] == menos:
        print(f'[{c[0]}] ', end='')
