# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas letras maiúsculas e minúsculas.
# > Quantas letras ao todo (sem considerar espaços).
# > Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ')

print('Nome com todas letras maiúsculas:', nome.upper())
print('Nome com todas letras maiúsculas:', nome.lower())
print('Quantas letras seu nome completo possui: ', len(nome) - nome.count(' '))
dividido = nome.split()
print('Quantas letras tem seu primeiro nome:',len(dividido[0]))
#Outra maneira
#print('Seu primeiro nome tem {nome.find(' ')} letras')
