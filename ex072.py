# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por
# extenso.

numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','desesseis','desessete','dezoito','desenove','vinte')
numero = int(input('Digite um número de 0 a 20: '))
while numero < 0 or numero > 20:
    print('Número inválido, tente novamente.')
    numero = int(input('Digite um número de 0 a 20: '))
if numero >= 0 and numero <= 20:
    print(f'Você digitou o número {numeros[numero]}.')
