# Faça um programa que leia algo pelo teclado e moestre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

n = input('Digite algo: ')
print(type(n))
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('É numérico?', n.isnumeric())
print('É espaço?', n.isspace())
print('É minúsculo?', n.islower())
print('É maiúsculo?', n.isupper())
