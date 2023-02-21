# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5%
# de desconto.

preco = float(input('Digite o preço atual do produto: '))
desconto = preco * 0.05
# Outro exemplo: desconto = preco * 5 / 100
print(f'O preço com desconto é de R$ {preco-desconto:.2f}')
