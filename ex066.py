# Crie um programa que leia vários números inteiros pelo teclado. O programa só
# vai parar quando o usuário digitar o valor 999, que é a condição de parada. No
# final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).
# Igual ao ex064, mas este foi após a aula que ensina o comando break para sair
# de loopings infinitos.

quant = soma = 0

while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    quant += 1
    soma += numero
print(f'A soma dos {quant} valores é {soma}.')