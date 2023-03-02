# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
# com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoNasc = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - anoNasc

print(f'Nascidos em {anoNasc} completam {idade} anos em {date.today().year}.')

if idade < 18:
    if 18 - idade == 1:
        print('Falta apenas 1 ano para o seu alistamento, prepare-se!')
    else:
        print(f'Faltam {18 - idade} anos para o seu alistamento.')
elif idade == 18:
    print('Chegou a hora de se alistar! Se apresente na sua Junta de Serviço Militar mais próxima!')
else:
    print(f'Já se passou {idade - 18} anos do momento do seu alistamento.')
    print(f'Seu alistamento foi em {date.today().year - (idade - 18)}.')
    print('Caso não tenha se alistado ainda, apresente-se na junta militar mais próxima para regularizar sua situação.')