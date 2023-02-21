# Escreva um programa que pergunte o salário de um funcionário e calcule o valor
# do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para salários inferiores a R$1.250,00 ou iguais, o aumento é de 15%.

cores = {'limpa':'\033[m','azul':'\033[0;34m','ciano':'\033[0;36m','verdeNeg':'\033[1;32m','verdeFdAmarelo':'\033[1;32;43m'}
salario = float(input('Digite o salário do funcionário: '))
if salario > 1250:
    print(f'{cores["azul"]}O aumento será de {cores["verdeNeg"]}10%{cores["azul"]} e seu salário ficará {cores["verdeFdAmarelo"]}R${salario + salario * 0.10:.2f}{cores["limpa"]}.')
else:
    print(f'{cores["ciano"]}O aumento será de {cores["verdeNeg"]}15%{cores["ciano"]} e seu salário ficará {cores["verdeFdAmarelo"]}R${salario + salario * 0.15:.2f}{cores["limpa"]}.')
