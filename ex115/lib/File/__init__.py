# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu
# nome e idade em um arquivo d texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as 
# pessoas cadastradas.

from lib.interface import *
from lib.interface import *

def checkFile(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def createFile(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {name} criado com sucesso.')

def readFile(name):
    try:
        a = open(name, 'rt')
    except:
        print('Erro ao tentar ler o arquivo.')
    else:
        header('PESSOAS CADASTRADAS')
        for l in a:
            data = l.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<30}{data[1]:>3} anos')
    finally:
        a.close()

def newRegister(file, nome='desconhecido', idade=0):
    try:
        a = open(file, 'at')
    except:
        print('Houve um ERRO ao abrir o arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            a.close()