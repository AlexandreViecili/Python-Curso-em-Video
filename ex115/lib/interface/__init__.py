# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu
# nome e idade em um arquivo d texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as 
# pessoas cadastradas.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO! Comando interrompido pelo usuário.\033[m')
            return 0
        else:
            return n

def line(tam = 42):
    return '-' * tam

def header(txt):
    print(line())
    print(txt.center(42))
    print(line())

def menu(lista):
    header('MENU')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c += 1
    print(line())
    opt = leiaInt('Sua Opção: ')
    return opt