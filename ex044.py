# Elabore um programa que calcule o valor a ser pago por um produto, considerando
# o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

preco = float(input('Digite o preço do produto: R$'))
print('Digite a opção correspondente a forma de pagamento:')
opcao = int(input('''1 = À vista/Pix
2 = À vista no Cartão
3 = Em até 2x no Cartão
4 = 3x ou mais no Cartão
Qual opção? '''))
if opcao == 1:
    print(f'À vista/Pix com 10% de desconto: R${preco - preco * 0.10:.2f}')
elif opcao == 2:
    print(
        f'À vista no Cartão com 5% de desconto: R${preco - preco * 0.05:.2f}')
elif opcao == 3:
    print(
        f'Em até 2x sem acréscimo: Mensalidades de R${preco / 2:.2f} por mês e um total de R${preco:.2f}.')
elif opcao == 4:
    parcelas = int(input('Quantidade de parcelas: '))
    print(
        f'3x ou mais no Cartão com acréscimo de 20%: Mensalidades de R${(preco + preco * 0.20) / parcelas:.2f} por mês e um total de R${preco + preco * 0.20:.2f}.')
else:
    print('Opção inválida.')
