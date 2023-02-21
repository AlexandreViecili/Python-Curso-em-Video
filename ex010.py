# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos Dólares ela pode comprar.

reais = float(input('Quantos reais você tem na carteira? '))
dolar = reais / 5.17
print(f'Você pode comprar ${dolar:.2f}.')
