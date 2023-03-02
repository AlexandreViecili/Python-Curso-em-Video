# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
# e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura em Metros: '))

imc = peso / (altura * altura)

print(f'Seu IMC é de {imc:.1f}.')

if imc < 18.5:
    print('Abaixo do Peso.')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal.')
elif imc >= 25 and imc < 30:
    print('Sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Obesidade.')
else:
    print('Obesidade Mórbida.')