# Crie um programa onde o usuário possa digitar cinco valores números e 
# cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()).
# No final, mostre a lista ordenada na tela.

numeros = []

for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Número adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Número adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {numeros}')
