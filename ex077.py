# Crie um programa que tenha uma tupla com várias palavras (não usar
# acentos). Depois disso, você deve mostrar, para cada palavra, quais são
# suas vogais.

palavras = ('Python', 'Inteligencia', 'Artificial',
            'Big', 'Data', 'Analise', 'Dados')

for c in palavras:
    print(f'Na palavra {c.upper()} temos as vogais', end='')
    for letra in c:
        if letra.upper() in 'AEIOU':
            print(f' {letra.lower()}', end='')
    print('')
