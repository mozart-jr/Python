# Desafio 48
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 a 500.

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print(f'FA soma de todos os {cont} valores solicitados é {soma}')
