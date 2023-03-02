# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do
# programa, mostre:
# >A média de idade do grupo.
# >Qual é o nome do homem mais velho
# >Quantas mulheres tem menos de 20 anos.

soma = 0
idadeMais = 0
velho = ''
menor20 = 0
for i in range(1, 5):
    print(f'---- {i}ª PESSOA ----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    soma += idade
    sexo = input('Sexo [M/F]: ').upper().strip()
    if idade > idadeMais and sexo == 'M':
        idadeMais = idade
        velho = nome
    if sexo == 'F' and idade < 20:
        menor20 += 1
print(f'A média de idade do grupo é {soma / 4:.1f}.')
print(f'{velho} é o homem mais velho do grupo com {idadeMais} anos.')
print(f'A quantidade de mulheres menores de 20 anos é {menor20}.')