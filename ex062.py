# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais
# alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termos = 1
fimtermo = 11
opcao = 1
while opcao != 0:
    while termos != fimtermo:
        print(f'{termos}° termo: {pt}')
        pt = pt + r
        termos += 1
    opcao = int(input('Mais quantos termos você quer ver? '))
    fimtermo += opcao
    

