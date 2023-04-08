# Faça um programa que tenha uma função chamada escreva(), que receba um texto
# qualquer como parâmetro e mostre uma mensagem com tamanho adatável.
# Ex:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~~~~~

def escreva(txt):
    print(f'~' * (len(txt) + 4))
    print(f'  {txt}')
    print(f'~' * (len(txt) + 4))


# Programa Principal
escreva('Alexandre Pinheiro')
escreva('Curso de Python no Youtube')
escreva('CeV')
