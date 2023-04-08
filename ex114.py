# Crie um código em Python que teste se o site pudim.com.br está acessível pelo
# computador usado.

import urllib
import urllib.request
import webbrowser   # Adcionei a função de abrir o site no navegador.

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Não foi possível acessar o site Pudim.')
else:
    print('Consegui acessar o site Pudim!')
    webbrowser.open('http://www.pudim.com.br')
