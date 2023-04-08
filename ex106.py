# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai
# digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra
# 'FIM', o programa se encerrará.
# OBS: use cores.

cores = {'limpa':'\033[m', 'intro':'\033[0;30;43m', 'time':'\033[0;30;44m', 'help':'\033[7;30;40m', 'fim':'\033[0;30;41m'}
#

def texto(txt, cor):
    print(cores[cor], end='')
    print(f'~' * (len(txt) + 4))
    print(f'  {txt}')
    print(f'~' * (len(txt) + 4))
    print(cores['limpa'], end='')


def pyhelp(cmd):
    print(cores['help'], end='')
    help(cmd)
    print(cores['limpa'], end='')
    

# Programa Principal
while True:
    texto('SISTEMA DE AJUDA PyHELP', 'intro')
    a = str(input('Função ou Biblioteca > ')).lower().strip()
    if a == 'fim':
        texto(f'ATÉ LOGO!', 'fim')
        break
    texto(f"Acessando o manual do comando '{a}'", 'time')
    pyhelp(a)
    

