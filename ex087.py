# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

somaPares = soma3C = maior2L = 0

print('=' * 60)
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
soma3C = matriz[0][2] + matriz[1][2] + matriz [2][2]
for c in matriz[1]:
    if c > maior2L:
        maior2L = c
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=' * 60)
print(f'A soma dos valores pares é {somaPares}.')
print(f'A soma dos valores da terceria coluna é {soma3C}.')
print(f'O maior número da segunda linha é {maior2L}.')