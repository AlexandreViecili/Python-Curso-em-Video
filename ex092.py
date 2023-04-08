# Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-os (com idade) em um dicionário se por acaso a CTPS for 
# diferente de ZERO, o dicionário receberá também o ano de contratação
# e o salário. Calcule e acrescente, além da idade, com quantos anos
# a pessoa vai se aposentar.
# Considere neste exercício 35 anos de contribuição para se aposentar
# independente de sexo.

from datetime import date


cadastro = {}
hoje = date.today().year

while True:
    cadastro['nome'] = str(input('Nome: '))
    cadastro['idade'] = hoje - int(input('Ano de Nascimento: '))
    cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if cadastro['ctps'] == 0:
        break
    else:
        cadastro['contratação'] = int(input('Ano de Contratação: '))
        cadastro['salario'] = float(input('Salário: R$ '))
        cadastro['aposentadoria'] = (cadastro['contratação'] - (hoje - cadastro['idade'])) + 35
        break
print('=-' * 30)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')