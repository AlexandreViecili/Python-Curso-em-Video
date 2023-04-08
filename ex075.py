# Desenvovla um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))

print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 not in numeros:
    print(f'O valor 3 foi digitado em nenhuma posição.')
else:
    print(f'O valor 3 foi digitado na {numeros.index(3) + 1}ª posição.')
print('Os valores pares digitados foram ', end='')
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0 and numeros[c] != 0:
        print(numeros[c], end=' ')