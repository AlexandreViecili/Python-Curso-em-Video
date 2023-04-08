# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu
# nome e idade em um arquivo d texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as 
# pessoas cadastradas.

from lib.interface import *
from lib.File import *
from time import sleep

file = 'Cadastros'

if not checkFile(file):
    createFile(file)

while True:
    r = menu(['Ver Pessoa Cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if r == 1:
        # Abrir lista de pessoas cadastradas.
        readFile(file)
    elif r == 2:
        # Cadastrar uma nova pessoa.
        header('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        newRegister(file, nome, idade)
    elif r == 3:
        # Encerrar o programa.
        print('\033[32mEncerrando o programa, obrigado pela preferência!\033[m')
        break
    else:
        # Digitou uma opção errada.
        print('\033[31mERRO: Digite uma opção válida.\033[m')
    sleep(2)

