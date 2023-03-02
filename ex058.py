# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre
# 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando
# no final quantos palpites foram necessários para vencer.

from random import randint

tentativas = 0
computador = randint(0, 1000)
jogador = int(input('Tente adivinhar um número de 0 a 1000 que o computador pensou: '))
while jogador != computador:
    if jogador < computador:
        print(f'''Mais... Não foi dessa vez! :(''')
        jogador = int(input('Tenta novamente: '))
        tentativas += 1
    elif jogador > computador:
        print(f'''Menos... Não foi dessa vez! :(''')
        jogador = int(input('Tenta novamente: '))
        tentativas += 1
if jogador == computador:
    print(f'''Parabéns! Você acertou! :D 
Número de Tentativas: {tentativas}''')
