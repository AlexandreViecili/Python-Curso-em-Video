# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.
# Ex: Apos a sopa

print('Para executar a minha solução digite 1, para executar a do Guanabara digite 2.')
escolha = int(input('Digite sua opção: '))

if escolha == 1:

# Minha solução

    frase = input('Digite uma frase: ')
    f = frase.upper().replace(' ', '')
    l = len(f) - 1

    palin = True
    for i in range(1 ,round(l/2)):     
        if f[l-i] == f[i]:
            palin = True
        else:
            palin = False
    if palin == False:
        print('A frase NÃO é um palíndromo.')
    else:
        print('A frase É um palíndromo.')

elif escolha == 2:

# Solução Guanabara

    frase = str(input('Digite uma frase: ')).strip().upper()
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = ''
    for letra in range(len(junto) - 1, - 1, - 1):
        inverso += junto[letra]
    print(f'{inverso}  {junto}')
    if inverso == junto:
        print('Temos um Palíndromo.')
    else:
        print('A frase digita não é um palíndromo.')

else:
    print('Opção inválida.')