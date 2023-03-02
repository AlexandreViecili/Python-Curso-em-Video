# Faça um programa que calcule a soma entre todos os números ímpares que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
quant = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        quant += 1

print(f'Há {quant} valores ímpares múltiplos de 3 no intervalo de 1 até 500 e a soma de todos eles é {soma}.')