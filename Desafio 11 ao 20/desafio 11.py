# Desafio 11
# Faça um programa que leia a largura e a altura de uma parede em metros quadrados, calcule a sua área,
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input('Informe a largura: '))
altura = float(input('Informe a altura: '))
area = largura * altura
print(f'esta parede tem {area}m²')
print(f'Precisará de {area / 2} latas de tinta ')
print('Fim! ')
