# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando
# uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

cores = {'limpa':'\033[m', 'vermelho':'\033[0;31m','amarelo':'\033[0;33m','verde':'\033[0;32m'}

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))

media = (n1 + n2) / 2

if media < 5.0:
    print(f'Média: {media:.1f}\n{cores["vermelho"]}REPROVADO!!!{cores["limpa"]}')
elif media >= 5.0 and media <= 6.9:
    print(f'Média: {media:.1f}\n{cores["amarelo"]}RECUPERAÇÃO!{cores["limpa"]}')
else:
    print(f'Média: {media:.1f}\n{cores["verde"]}APROVADO!!!{cores["limpa"]}')