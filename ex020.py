# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de
# trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre
# a ordem sorteada.

import random

aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

print('A ordem de apresentação dos alunos será:')
random.shuffle(alunos)
print(alunos)