# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo
# chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de
# funcionar como a função input(), mas com uma validação de dados para aceitar
# apenas valores que sejam monetários.

def leiaDinheiro(msg):
    ok = False
    while not ok:
        n = str(input(msg)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'\033[0;31mERRO: "{n}" é um preço inválido!\033[m')
        else:
            ok = True
            return float(n)