# Crie um programa que tenha uma tupla única com nomes de produtos e seus
# respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma
# tabular.

lista = ('Placa de Vídeo RTX 3060 Asus', 2399.99, 'Processador AMD Ryzen 7 5700x', 1399.99, 'Memória Corsair 32GB', 419.99,
         'SSD Kingston NV2 500GB', 242.99, 'Fonte Corsair 750W', 579.99, 'Water Cooler Rise Mode', 259.99, 'Gabinete Gamer Redragon', 349.99)
print('-' * 70)
print(f'{"LISTAGEM DE PREÇO" : ^70}')
print('-' * 70)
for c in range(0, len(lista), 2):
    print(f'{lista[c]:.<59}', end='')
    print(f'R$ {lista[c + 1]: >7}')
print('-' * 70)
