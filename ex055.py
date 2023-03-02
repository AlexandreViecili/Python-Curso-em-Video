# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
# o maior e o menor peso lidos.

print('Para escolher a minha solução digite 1, para escolher solução do Guanabara digite 2.')
escolha = int(input('Digite sua escolha: '))

if escolha == 1:

# Minha solução:

    maior = 0
    menor = 300
    for i in range(1, 6):
        peso = float(input(f'Digite o peso da {i}ª pessoa em kg: '))
        if peso > maior:
            maior = peso
        if menor > peso:
            menor = peso
    print(f'''Maior Peso: {maior:.1f}
Menor Peso: {menor:.1f} ''')

elif escolha == 2:

# Solução Guanabara:

    maior = 0
    menor = 0
    for p in range(1, 6):
        peso = float(input(f'Peso da {p}ª pessoa: '))
        if p == 1:
            maior = peso
            menor = peso
        else:
            if peso > maior:
                maior = peso
            if peso < menor:
                menor = peso
    print(f'O maior peso lido foi de {maior}Kg.')
    print(f'O menor peso lido foi de {menor}Kg.')

else:
    print('Opção inválida.')