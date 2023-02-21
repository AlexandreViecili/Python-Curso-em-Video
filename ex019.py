# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça
# um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')
#Poderia também fazer uma lista = [aluno1, aluno2, aluno3, aluno4]'
#Então ficaria escolha = choice(lista)
escolha = choice([aluno1, aluno2, aluno3, aluno4])
print(f'O aluno escolhido para apagar o quadro foi {escolha}.')