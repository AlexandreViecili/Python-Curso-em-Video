# Faça um programa que leia 5 valores númerico e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas 
# respectivas posições na lista.

numeros = []
for c in range(0, 5):
    numeros.append(int(input(f"Digite um valor para a posição {c}: ")))
print(f'Você digitou os números {numeros}')
print(f'O maior valor digitado foi {max(numeros)} nas posições ', end='')
for a, b in enumerate(numeros):
    if b == max(numeros):
        print(f'{a}... ', end='')
print(f'\nO menor valor digitado foi {min(numeros)} nas posições ', end='')
for a, b in enumerate(numeros):
    if b == min(numeros):
        print(f'{a}... ', end='')