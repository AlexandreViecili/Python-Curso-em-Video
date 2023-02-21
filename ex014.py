#Escreva um programa que converta uma temperatura digita em ºC e converta para ºF.
# Adcionei ºK também.

celsius = float(input('Informe a temperatura atual: '))
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15
print(f'A temperatura atual de {celsius}ºC corresponde a {fahrenheit}ºF e {kelvin} K.')
