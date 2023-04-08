# Crie um programa que tenha uma função chamada voto() que vai receber como
# parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.



def voto(nasc):
    from datetime import datetime
    hoje = datetime.today().year
    idade = hoje - nasc
    if idade >= 16 and idade < 18 or idade >= 70:
        return f'Com {idade} anos: VOTO FACULTATIVO.'
    elif idade >= 18 and idade < 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: NÃO VOTA'


nascimento = int(input('Ano de Nascimento: '))
print(voto(nascimento))