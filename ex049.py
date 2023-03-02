# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
# OBS: Já utilizei laço for no DESAFIO 09, neste irei acrescentar também a função
# do usuário poder escolher também até qual número ele quer ver a tabuada.

n = int(input('Digite o número que você quer ver a tabuada: '))
t = int(input('Digite até qual tabuada você quer ver: '))

for i in range(1, t+1):
    print(f'{n} x {i} = {n * i}')