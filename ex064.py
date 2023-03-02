# Crie um programa que leia vários números inteiros pelo teclado. O programa só
# vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

numero = 0
totnumeros = 0
soma = 0
print('''=============== SOMADOR ===============
caso queira parar de somar digite 999.''')
while numero != 999:
    numero = int(input('Digite um número: '))
    if numero != 999:
        totnumeros += 1
        soma += numero
    else:
        print('Você parou a soma.')
print(f'Você digitou um total de {totnumeros} e a soma total deles é {soma}.')
