# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.

salario = float(input('Digite o salário atual: R$ '))
aumento = salario * 0.15
print(f'O novo salário é de R$ {salario+aumento:.2f}')
