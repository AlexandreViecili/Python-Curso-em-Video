# Crie um programa que vai ler vários numeros e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares 
# e os valores ímpares digitados, rescpectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um número: ')))
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Opção inválida.')
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')