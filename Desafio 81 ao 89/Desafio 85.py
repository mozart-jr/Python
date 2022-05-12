# Exercício Python 085:
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


lista_numeros = [[], []]

for n in range(0, 7):
    num = int(input(f'Digite o {n + 1}º número:  '))

    if num % 2 == 0:     # Números Pares
        lista_numeros[0].append(num)
    else:                # Números Ímpares
        lista_numeros[1].append(num)

print(f'Par: {lista_numeros[0]} ')
print(f'Ímpar: {lista_numeros[1]} ')
print('-' * 30)
print('EM ORDEM CRESCENTE: ')
print('-' * 30)
print(f'Par: {sorted(lista_numeros[0])}')
print(f'Ímpar: {sorted(lista_numeros[1])} ')


# lista_num = [[], []]
# valor = 0
#
# for c in range(0, 7):
#     valor = int(input(f'Digite o {c + 1}º número: '))
#
#     if valor % 2 == 0:
#         lista_num[0].append(valor)
#     else:
#         lista_num[1].append(valor)
#
# print('-' * 30)
# print(f'Números digitados: {lista_num}')
# print('-' * 30)
#
# # -------------- Utilizando o comando sorted() -------
# print(f'Números PARES: {sorted(lista_num[0])}')
# print(f'Números ÍMPARES: {sorted(lista_num[1])}')

# -------------- Utilizando o comando .sort() --------
# num[0].sort()
# num[1].sort()
# print(f'Números PARES: {num[0]}')
# print(f'Números ÍMPARES: {num[1]}')

