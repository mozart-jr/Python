 Desafio 50
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
 # Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'digite o {c}º número: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print(f'Você informou {cont} número(s) PARES e a soma foi {soma}')
