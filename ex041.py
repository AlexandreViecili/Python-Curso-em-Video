# A confederação Nacional de Natação precisa de um programa que leia o ano de 
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER

from datetime import date

anoNasc = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - anoNasc

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Categoria: MIRIM.')
elif idade > 9 and idade <= 14:
    print('Categoria: INFANTIL.')
elif idade > 14 and idade <= 19:
    print('Categoria: JUNIOR.')
elif idade > 20 and idade <=25:
    print('Categoria: SÊNIOR.')
else:
    print('Categoria: MASTER.')
