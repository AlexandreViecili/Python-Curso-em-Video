# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa
# vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
# para cada jogo, cadastrando tudo em uma lista composta.

from time import sleep
from random import randint

temp = []
main = []

print('=' * 60)
print(f'{"GERADOR DE JOGOS DA MEGA SENA":^60}')
print('=' * 60)

jogos = int(input('Quantos jogos você quer sortear? '))

for c in range(0, jogos):
    for b in range(0, 6):
        n = randint(1, 60)
        for a in temp:
            while n == a:
                n = randint(1, 60)
        temp.append(n)
        temp.sort()
    main.append(temp[:])
    temp.clear()

print(f'{f"SORTEANDO OS {jogos} JOGOS":-^60}')

for d in range(0, jogos):
    print(f'Jogo {d+1}: {main[d]}')
    sleep(1)
print(f'{"BOA SORTE!!!":=^60}')
