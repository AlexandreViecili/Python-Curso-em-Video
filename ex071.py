# Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
# pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
# vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

saque = int(input('Qual valor você deseja sacar? R$'))
total = saque
ced = 50
quantC = 0
while True:
    if total >= ced:
        total -= ced
        quantC += 1
    else:
        if quantC > 0:
            print(f'Cédulas de R${ced}: {quantC}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        quantC = 0
        if total == 0:
            break
