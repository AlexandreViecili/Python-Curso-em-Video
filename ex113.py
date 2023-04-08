# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a 
# possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma finção leiaFloat() com a mesma funcionalidade.

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
    

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO! Comando interrompido pelo usuário.\033[m')
            return 0
        else:
            return n
        
    

n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {n1} e o número real {n2}.')   