# Desafio 17
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
# Obs: hypot  é para calcular a hipotenusa.

#formula da Hipotenusa -> H² = Co² + Ca²
#Raiz quadrada = (1/2)
#H = (co² + ca²) ** (1/2)

co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
hyp = (co ** 2 + ca ** 2) ** (1/2)
print(f'O valor da hipotenusa é {hyp:.2f}')
print('FIM !!')

################################## ###### ou #############################################

from math import hypot
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
print(f'O valor da hipotenusa é {hypot(co, ca):.2f}!')
