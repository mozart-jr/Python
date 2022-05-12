# Desafio 30
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print('-' * 58)
print('Digite um número inteiro para saber se ele é Par ou Ímpar: ')
print('-' * 58)

numero = int(input('Número: '))
if numero % 2 == 0:
    print(f'O número {numero} é PAR. ')
else:
    print(f'O número {numero} é ÍMPAR. ')