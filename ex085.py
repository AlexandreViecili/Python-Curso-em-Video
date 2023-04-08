# Crie um programa onde o usuário possa digitar sete valores núméricos e 
# cadastre-os em uma lista única que mantenha separados os valores pares e
# ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

princ = []
pares = []
impares = []

for c in range(7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
impares.sort()
princ.append(pares[:])
princ.append(impares[:])

print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')