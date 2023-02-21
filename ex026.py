# Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A"/
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a última vez.

frase = input('Digite um frase: ').upper().strip()
print('Quantas letras A a frase possui: ', end = '')
print(frase.count('A'))
print('Em que posição aparece o primeiro "A"? ', end = '')
print(frase.find('A') + 1)
print('Em que posição aparece o último "A"? ', end = '')
print(frase.rfind('A') + 1)