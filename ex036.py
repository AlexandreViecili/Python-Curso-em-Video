# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos
# anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do 
# salário ou então o empréstimo será negado.

cores = {'limpa':'\033[m', 'amarelo':'\033[0;33m','verde':'\033[0;32m','vermelho':'\033[0;31m'}
casa = float(input(f'{cores["amarelo"]}Qual o valor da casa? {cores["limpa"]}'))
salario = float(input(f'{cores["amarelo"]}Qual o salário do comprador? {cores["limpa"]}'))
anos = int(input(f'{cores["amarelo"]}Em quantos anos será paga a casa? {cores["limpa"]}'))
valorPrest = casa / (anos * 12)
salario30P = salario * 0.30
if valorPrest > salario30P:
    print(f'{cores["vermelho"]}EMPRÉSTIMO NEGADO.{cores["limpa"]} Valor da prestação superior a 30% do salário do comprador')
    print(f'{cores["amarelo"]}Valor da prestação:{cores["limpa"]} R${valorPrest:.2f}.')
    print(f'{cores["amarelo"]}30% do salário:{cores["limpa"]} R${salario30P:.2f}.')
else:
    print(f'{cores["verde"]}EMPRÉSTIMO APROVADO!')
    print(f'{cores["amarelo"]}Valor da prestação: {cores["limpa"]}R${valorPrest:.2f}.')
    