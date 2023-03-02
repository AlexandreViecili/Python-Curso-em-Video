# Faça um programa que mostra a tabuada de vários números, um de cada vez, para
# cada valor digitado pelo usuário. O programa será interrompido quanto o número
# solicitado for negativo.

n = t = 0

while True:
    n = int(input('A tabuada de qual número você deseja ver? '))
    print('')
    t = 0
    if n < 0:
        break
    while t < 10:
        prod = n * (t + 1)
        print(f'{n} x {t + 1} = {prod}')
        t += 1
    print('')
print('Programa de Tabuada encerrado, obrigado por usar!\n')
