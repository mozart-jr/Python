# Desafio 12
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = str(input('nome do produto:')).upper()
preco_normal = float(input('Preço: '))
desconto = 0.95
print(f'O preço desse produto com 5% de desconto é {preco_normal * desconto}')
print('FIM!!')