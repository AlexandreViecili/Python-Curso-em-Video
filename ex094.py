# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
# dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No
# final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

ficha = {}
cadastros = []

totCad = totidade = 0
escolha = ''

while True:
    ficha['nome'] = str(input('Nome: ')).strip()
    ficha['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while ficha['sexo'] not in 'MF':
        print('Opção inválida. Digite apenas M ou F.')
        ficha['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    idade = ficha['idade'] = int(input('Idade: '))
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Opção inválida. Digite apenas S ou N.')
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    cadastros.append(ficha.copy())
    ficha.clear()
    totCad += 1
    totidade += idade
    if escolha == 'N':
        break
media = totidade / totCad
print(f'O grupo tem {totCad} pessoas.')
print(f'A média de idade é de {media:.2f} anos')
print('As mulheres cadastradas foram: ', end='')
for p in cadastros:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('Lista de pessoas que estão acima da média de idade: ')
for p in cadastros:
    if p['idade'] > media:
        print()
        print(f'nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')
print('<< ENCERRADO >>')