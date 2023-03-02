# Crie um programa que leia vários números inteiros pelo teclado. No final da
# execução, mostre a média entre todos os valores e qual foi o maior e menor 
# valores lidos. O programa deve perguntar ao usuário se ele quer continuar a
# digitar valores.

opcao = ''
totnumeros = soma = maior = 0
menor = 999999999999
while opcao != 'N':
    numeros = float(input('Digite um número inteiro: '))
    totnumeros += 1
    soma += numeros
    if numeros > maior:
        maior = numeros
    if numeros < menor:
        menor = numeros
    opcao = str(input('Você quer digitar mais valores? [S/N] ')).upper()
media = soma / totnumeros
print(f'''A média de todos valores digitados foi {media:.2f}.
O maior valor digitado foi {maior}.
O menor valor digitado foi {menor}. ''')