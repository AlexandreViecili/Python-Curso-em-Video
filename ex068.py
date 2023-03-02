# Faça um programa que jogue par ou ímpar com o computador. O jogo só será
# interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.

from random import randint

print('=-=' * 10)
print('PAR OU ÍMPAR'.center(30))
print('=-=' * 10)

vitorias = 0
while True:
    numeroJ = int(input('Digite um número de 0 a 10: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    numeroC = randint(0, 11)
    total = numeroJ + numeroC
    if escolha == 'P' and total % 2 == 0:
        print(f'''Você jogou {numeroJ} e o computador {numeroC}.
O total é {total} e deu PAR.''')
        print('''Você VENCEU!
Vamos jogar novamente...''')
        print('=-=' * 10)
        vitorias += 1
    elif escolha == 'I' and total % 2 == 1:
        print(f'''Você jogou {numeroJ} e o computador {numeroC}.
O total é {total} e deu ÍMPAR.''')
        print('''Você VENCEU!
Vamos jogar novamente...''')
        print('=-=' * 10)
        vitorias += 1
    elif escolha == 'I' and total % 2 == 0:
        print(f'''Você jogou {numeroJ} e o computador {numeroC}.
O total é {total} e deu PAR.''')
        print(f'''Você PERDEU!
FIM DE JOGO! Você venceu {vitorias} vezes.''')
        print('=-=' * 10)
        break
    else:
        print(f'''Você jogou {numeroJ} e o computador {numeroC}.
O total é {total} e deu ÍMPAR.''')
        print(f'''Você PERDEU!
FIM DE JOGO! Você venceu {vitorias} vezes.''')
        break
