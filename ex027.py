# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente.

nome = input('Digite o seu nome completo: ')
espacos = nome.count(' ')
dividido = nome.split()
print('Primeiro nome:', dividido[0])
print('Último nome:', dividido[espacos])
# Outra maneira de fazer a última linha:
#print('Último nome:', dividido[len(dividido) - 1])