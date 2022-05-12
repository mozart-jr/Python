# Desafio 10
# Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = int(input('Quantos Reais você tem na carteira: R$ '))
dolar = float(input('Informe o valor do dolar na data de hoje: R$ '))
compra = carteira / dolar
print(f'Com R$ {carteira:.2f} na carteira, da para comprar $ {compra:.2f} ')