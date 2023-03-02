# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

total = prod1000 = cont = menor = 0
barato = escolha = ''

while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: '))
    cont += 1
    total += preco
    if preco > 1000:
        prod1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'''O total da compra é R${total:.2f}.    
Total de produtos acima de R$1000: {prod1000}
Nome do produto mais barato: {barato}''')
