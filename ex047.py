# Crie um programa que mostre na tela dos os números pares que estão no intervalo
# entre 1 e 50.

for i in range(1, 51):
    if i % 2 == 0:          # Desta maneira o computador faz iterações 
        print(i, end=' ')   # desnecessárias a mais fazendo o processador
print('Fim.')               # trabalhar mais.

for i in range(2, 51, 2):   # Desta maneira apenas faz as iterações
    print(i, end=' ')       # necessárias, otimizando o processamento.
print('Fim.')
