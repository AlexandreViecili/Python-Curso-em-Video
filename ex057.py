# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M'
# ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper().strip()[0]
while sexo != "M" and sexo != "F": #while sexo not in 'MmFf': Também é uma forma de fazer esta mesma checagem.
    sexo = str(input('Opção inválida, digite "M" para masculino ou "F" para feminino: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado')
