#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros
# e milímetros

metros = int(input('Quantos metros? '))
print(f'A medida de {metros:.1f}m corresponde a: ')
print(f'{metros/1000}km')
print(f'{metros/100}hm')
print(f'{metros/10}dam')
print(f'{metros*10}dm')
print(f'{metros*100}cm')
print(f'{metros*1000}mm')
