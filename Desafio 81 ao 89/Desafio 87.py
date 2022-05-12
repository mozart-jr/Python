# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma = maior = 0
for lin in range(0, 3):
    for col in range(0, 3):
        num = (int(input(f'Informe o valor [{col, lin}]: ')))
        matriz[lin][col] = num
print('=' * 30)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[ {matriz[lin][col]:^5}', end='')
        if matriz[lin][col] % 2 == 0:
            pares = pares + matriz[lin][col]
    soma = soma + matriz[lin][2]
    print()
maior = max(matriz[1][0], matriz[1][1], matriz[1][2])
print('=' * 30)
print(f'A soma dos valores pares vale {pares}')
print(f'A soma dos valores da 3ª coluna vale {soma}')
print(f'O maior valor da 2ª coluna vale {maior}')
