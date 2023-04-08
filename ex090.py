# Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela.

boletim = {}
boletim['Nome'] = str(input('Nome: ')).strip()
boletim['Média'] = float(input(f'Média de {boletim["Nome"]}: '))
if boletim['Média'] >= 7:
    boletim['Situação'] = 'Aprovado'
elif 5 <= boletim['Média'] < 7:
    boletim['Situação'] = 'Recuperação'
else:
    boletim['Situação'] = 'Reprovado'
for k, v in boletim.items():
    print(f'{k} é igual a {v}')