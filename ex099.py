# Faça um programa que tenha uma função chamada maior(), que receba vários 
# parâmetros com valores inteiros.
# Seus programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(* n):
    print('=<>=' * 15)
    print('Analisando os valores passados...')
    if len(n) == 0:
        m = 0
    else:
        m = n[0]
    for v in n:
        if v > m:
            m = v
        print(v, end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {len(n)} valores ao todo.')
    print(f'O maior valor informado foi {m}.')

maior(2, 9, 7, 0, 5)
maior(5, 3, 2, 8, 4)
maior(0, 5)
maior()