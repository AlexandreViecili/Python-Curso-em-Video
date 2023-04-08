# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa que vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols 
# feitos durante o campeonato.

dados = {}
golsP = list()

dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
total = 0
for c in range(0, partidas):
    golsP.append(int(input(f'Quantos gols na partida {c}? ')))    
dados['gols'] = golsP[:]
for c in golsP:
    total += c
dados['total'] = total
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for a in range(0, partidas):
    print(f'    => Na partida {a}, fez {dados["gols"][a]} gols.')
print(f'Foi um total de {dados["total"]} gols.')