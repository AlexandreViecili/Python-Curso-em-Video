# Escreva um programa que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

numero = int(input('Digite um número que você queira converter: '))
escolha = int(input('Digite 1 para converter para binário.\nDigite 2 para converter para octal.\nDigite 3 para converter para hexadecimal.\n'))
if escolha == 1:
    binario = str(bin(numero)[2:])
    print(f'O número {numero} convertido para binário é {binario}.')
elif escolha == 2:
    octal = str(oct(numero)[2:])
    print(f'O número {numero} convertido em octal é {octal}.')
elif escolha == 3:
    hexa = str(hex(numero)[2:])
    print(f'O número {numero} convertido em hexadecimal é {hexa}')
else:
    print('Opção inválida.')