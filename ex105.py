# Faça um programa que tenha uma função notas() que pode receber várias notas de
# alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adcione também as docstrings da função.


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com váris informações sobre a situação da turma.
    """
    ficha = {}
    ficha['total'] = len(n)
    ficha['maior'] = max(n)
    ficha['menor'] = min(n)                      
    ficha['média'] = sum(n) / len(n)
    if sit:
        if ficha['média'] >= 7:
            ficha['situação'] = 'BOA'
        elif ficha['média'] >= 6:
            ficha['situação'] = 'RAZOÁVEL'
        else:
            ficha['situação'] = 'RUIM'
        return ficha
    return ficha


# Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
