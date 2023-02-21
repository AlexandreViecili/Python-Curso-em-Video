# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.

cores = {'limpa':'\033[m','vermelho':'\033[0;31m','vermelhoSub':'\033[4;31m','verde':'\033[0;32m','verdeSub':'\033[4;32m','amarelo':'\033[33m'}
r1 = float(input(f'{cores["amarelo"]}Digite o comprimento em cm da primeira reta: '))
r2 = float(input('Digite o comprimento em cm da segunda reta: '))
r3 = float(input('Digita o comprimento em cm da terceira reta: '))
if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print(f'{cores["vermelho"]}Estas retas {cores["vermelhoSub"]}NÃO{cores["vermelho"]} podem formar um triângulo.{cores["limpa"]}')
else:
    print(f'{cores["verde"]}Estas retas podem {cores["verdeSub"]}SIM{cores["verde"]} formar um triângulo.{cores["limpa"]}')
