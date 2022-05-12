# Desafio 44
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# 	Avista dinheiro/cheque: 10% de desconto
# 	Avista no cartão: 5% de desconto
# 	Em até 2x no cartão: Preço normal
# 	3x ou mais no cartão: 20% de juros

preço = float(input('Total das compras: R$ '))
print('''Formas de Pagamento: 
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço * 0.9
elif opção == 2:
    total = preço * 0.95
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} SEM JUROS!')
elif opção == 4:
    total = preço * 1.2
    totparc = int(input('Quantas parcela? '))
    parcela = total / totparc
    print(f'Sua compra será parcela em {totparc}x de R$ {parcela:.2f} COM JUROS! ')
print(f'Sua compra de R$ {preço} vai custar R$ {total:.2f} no final.')
