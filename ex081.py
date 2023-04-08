# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, moestre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma descrescente.
# C) Se o valor 5 foi diigitado e está ou na lista.

numeros = []

escolha = ''
while True:
    numeros.append(int(input('Digite um número: ')))
    escolha = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    while escolha not in 'SN':
        print('Opção invalida.')
        escolha = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'N':
        break
print(f'Foram digitados um total de {len(numeros)} números.')
numeros.sort(reverse=True)
print(f'Os valores em ordem descrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')