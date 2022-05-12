# Desafio 9
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número para saber sua tabuada: '))
for contagem in range(1, 11):
    print(f'{num} x {contagem} = {num * contagem}')
print('Fim!')