# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em
# uma lista composta. No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.

main = []
alunos = []
notas = []

while True:
    alunos.append(str(input('Digite o nome do aluno: ')))
    for c in range(0, 2):
        notas.append(float(input(f'Nota {c+1}: ')))
    alunos.append(notas[:])
    notas.clear()
    escolha = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Opção inválida.')
        escolha = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    main.append(alunos[:])
    alunos.clear()
    if escolha == 'N':
        break
print('=' * 60)
print(f'No.   {"NOME":<30} MÉDIA')
print('-' * 45)
for c in range(len(main)):
    media = (main[c][1][0] + main[c][1][1]) / 2
    print(f'{c}', end='     ')
    print(f'{main[c][0]:<30}', end='')
    print(f'{media:>4.1f}')
print('-' * 50)
aluno = ''
while True:
    aluno = int(input('Quer ver as notas de qual aluno? (999 interrompe): '))
    while aluno != 999 and aluno not in range(0, len(main)):
        print(f'Aluno inválido. Digite de 0 à {len(main)-1}.')
        aluno = int(input('Quer ver as notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    print(f'Notas de {main[aluno][0]} são {main[aluno][1]}')
    print('-' * 50)
print('FINALIZANDO APLICATIVO...')
print('VOLTE SEMPRE O/')
