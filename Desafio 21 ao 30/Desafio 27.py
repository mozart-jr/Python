# Desafio 27
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# 	Ex: Ana Maria dos Santos
# o	primeiro = Ana
# o	ultimo = Santos

nome = str(input('Nome Completo: ')).split()

print(f'Primeiro nome: {nome[0].upper()}')
print(f'Último nome: {nome[-1].upper()}')