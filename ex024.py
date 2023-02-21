# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com
# o nome "SANTO"

cidade = input('Digite o nome da sua cidade: ')
cidade = cidade.upper()
print('Tem a palavra "Santo" na cidade? ')
print('SANTO' in cidade)