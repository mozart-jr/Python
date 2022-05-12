# Desafio 16
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6
## tunch -> descarta os valoeres depois da vírgula
## precisa importar da biblioteca math

from math import trunc
num = float(input('Informe um número Real: '))
print(f'A porção inteira do número Real {num} é {trunc(num)}')
print('Fim!')
