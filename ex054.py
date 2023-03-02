# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
# quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

anoAtual = date.today().year

maior = 0
menor = 0
print(anoAtual)
for i in range(1, 8):
    n = int(input(f'Digite a data de nascimento da {i}ª pessoa: '))
    if anoAtual - n < 21:
        menor += 1
    else:
        maior += 1
print(f'''Maiores de Idade: {maior}
Menores de Idade: {menor} ''')