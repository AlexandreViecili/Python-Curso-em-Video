# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
# Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista em ordem alfabética.
# D) Em que posição está o time a Chapecoense.

# Quando fiz esta atividade, o campeonato não tinha começado ainda, portanto
# escolhi a posição final do campeonato Brasileiro de 2019 aonde também a
# Chapecoense ainda estava na série A também.

times = ('Flamengo','Santos','Palmeiras','Grêmio','Athletico-PR','São Paulo','Internacional','Corinthians','Fortaleza','Goiás','Bahia','Vasco da Gama','Atlético-MG','Fluminense','Botafogo','Ceará SC','Cruzeiro','CSA','Chapecoense','Avaí')

print(f'=' * 60)
print(f'''Os cinco primeiros colocados de Brasileirão de 2019 foram:
{times[:5]}''')
print(f'=' * 60)
print(f'''Os quatro últimos colocados do Brasilerão de 2019 foram:
{times[16:]} ''')
print(f'=' * 60)
print(f'''Lista em órdem alfabética dos times do Brasileirão 2019:
{sorted(times)}''')
print(f'=' * 60)
print(f'''Chapecoense ficou na {times.index('Chapecoense') + 1}ª posição. ''')
