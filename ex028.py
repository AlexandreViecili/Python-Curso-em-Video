# Escreva um programa que faça o computador "pensar" em um número inteiro de 0 a 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

from random import randint
from time import sleep
numeroC = randint(0, 5)
print('=' * 71)
print('||  Tente adivinhar o número de 0 a 5 que o computador irá escolher. || ')
print('=' * 71)
numeroJ = int(input('Qual o número que o computador pensou? '))
print('PROCESSANDO...')
sleep(2)
print(f'O número escolhido pelo computador foi {numeroC}.')
if numeroJ == numeroC:
    print('Você adivinhou o número certo, parabéns!')
else:
    print('Não foi dessa vez, tenta novamente!')
