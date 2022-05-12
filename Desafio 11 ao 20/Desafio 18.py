# Desafio 18
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e a tangente desse ângulo.

import math
ang = int(input('Informe o ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print(f'O Seno {sen:.3f}')
print(f'O Cosseno {cos:.3f}')
print(f'A Tangente {tang:.3f}')
print('FIM !!')
