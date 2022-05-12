# Desafio 23
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# 	Ex: digite um número: 1834
# unidades: 4, dezenas: 3, centenas: 8, milhar: 1

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'A unidade é {u}')
print(f'A dezena é {d}')
print(f'A centena é {c}')
print(f'A milhar é {m}')
print('Fim!')