# Aprimore o DESAFIO 093 para que ele funcione com vários jogadres, incluindo
# um sistema de visualização de detalhes do aproveitamento de cada jogador.

dados = {}
golsP = []
dadosT = []

escolha = ''
while True:
    dados['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    total = 0
    for c in range(0, partidas):
        golsP.append(int(input(f'Quantos gols na partida {c}? ')))    
    dados['gols'] = golsP[:]
    
    for c in golsP:
        total += c
    golsP.clear()
    dados['total'] = total
    dadosT.append(dados.copy())
    dados.clear()
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Opção inválida.')
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('-=' * 30)
print(dadosT)
print('-=' * 30)
print('cod ', end='')
for o in dadosT[0].keys():
    print(f'{o:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(dadosT):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    jogador = int(input('Mostrar dados de qual jogador? '))
    if jogador == 999:
        break
    while jogador != 999 and jogador not in range(0, len(dadosT)):
        print(f'Erro! Não existe jogador com o código {jogador}! Tente novamente.')
        jogador = int(input('Mostrar dados de qual jogador? '))
    print(f'--  Levantamento do jogador {dadosT[jogador]["nome"]}:')
    for e, g in enumerate(dadosT[jogador]['gols']):
        print(f'No jogo {e} fez {g} gols.')
    print('-' * 40)    
print('<< VOLTE SEMPRE >>')
    