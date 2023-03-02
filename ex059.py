# Crie um programa que leia dois valores e mostre um menu na tela:
''' 
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
'''
# Seu programa deverá realizar a operação solicitada em cada caso.

print('-' * 28)
print('| CALCULADORA MULTI-FUNÇÃO |')
print('-' * 28)

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
escolha = 0
while escolha != 5:
    escolha = int(input('''O que você deseja fazer?
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Digite a opção que deseja: '''))
    if escolha == 1:
        print('-' * 28)
        print('|           SOMA           |')
        print('-' * 28)
        print(f'{n1} + {n2} = {n1 + n2}')
        print('')
    elif escolha == 2:
        print('-' * 28)
        print('|       MULTIPLICAÇÃO      |')
        print('-' * 28)
        print(f'{n1} x {n2} = {n1 * n2}')
        print('')
    elif escolha == 3:
        print('-' * 28)
        print('|           MAIOR           |')
        print('-' * 28)
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        else:
            print(f'{n1} NÃO é maior que {n2}')
        print('')
    elif escolha == 4:
        print('-' * 28)
        print('|       NOVOS NÚMEROS      |')
        print('-' * 28)
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print('')
    elif escolha == 5:
        print('Obrigado por usar o programa!')
    else:
        print('Opção inválida.')
    