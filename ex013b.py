# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.

preco = float(input('Preço atual do produto: '))
aVista = preco - (preco * 0.10)
aPrazo = preco + (preco * 0.08)
print(f'A vista o produto tem 10% de desconto e custará R$ {aVista:.2f}.')
print(
    f'Parcelado o produto tem 8% de acréscimo e custará um total de R$ {aPrazo:.2f}')
