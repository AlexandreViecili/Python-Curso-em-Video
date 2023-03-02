# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

cores = {'limpa':'\033[m', 'verde':'\033[0;32m', 'amarelo':'\033[0;33m', 'azul':'\033[0;34m', 'roxo':'\033[0;35m', 'ciano':'\033[0;36m', 'vermelho':'\033[0;31m'}
itens = (f'{cores["azul"]}Pedra{cores["limpa"]}',f'{cores["roxo"]}Papel{cores["limpa"]}',f'{cores["ciano"]}Tesoura{cores["limpa"]}')

print(f'{cores["verde"]}=' * 17)
print(f'|| {cores["amarelo"]}  JOKENPÔ  {cores["verde"]} ||')
print('=' * 17)

jogador = int(input(f'''{cores["limpa"]}Faça sua escolha!
{cores["azul"]}0 = Pedra
{cores["roxo"]}1 = Papel
{cores["ciano"]}2 = Tesoura
{cores["limpa"]}'''))

computador = randint(1, 3)

print(f'Você jogou {itens[jogador]}.')
print(f'O computador escolheu {itens[computador]}.')

if jogador == computador:
    print(f'{cores["amarelo"]}Empate! :o{cores["limpa"]}')
elif jogador - computador == -2 or jogador - computador == 1:
    print(f'{cores["verde"]}VOCÊ GANHOU! :D{cores["limpa"]}')
elif jogador - computador == 2 or jogador - computador == -1:
    print(f'{cores["vermelho"]}Você perdeu! :({cores["limpa"]}')
else:
    print(f'{cores["limpa"]}Opção inválida.')
