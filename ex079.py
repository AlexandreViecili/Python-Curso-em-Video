# Crie um programa onde o usuário possa digitar vários valores númericos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

numeros = []
escolha = ''
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com sucesso...')
    else:
        print('Número duplicado! Não será adicionado...')
    escolha = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        print('Opção inválida')  
        escolha = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')