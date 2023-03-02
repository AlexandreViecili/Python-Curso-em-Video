# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
# cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No
# final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

mais18 = quantH = menos20 = 0

while True:
    sexo = ''
    escolha = ''
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        quantH += 1
    if idade < 20 and sexo == 'F':
        menos20 += 1
    if escolha == 'N':
        break
print(f'''Pessoas maiores de 18 anos: {mais18}
Homens cadastrados: {quantH}
Mulheres menores de 20 anos: {menos20}''')
