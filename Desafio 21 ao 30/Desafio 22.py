# Desafio 22
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 	o nome com todas as letras maiúsculas;
# 	o nome com todas as letras minúscula;
# 	quantas letras ao todo (sem considerar espaços)
# 	quantas letras tem o primeiro nome.

nome = str(input('Informe o nome completo: '))
tamanho = nome.split()
print(f'Em letras maiúsculas: {nome.upper()} ')
print(f'Em letras minúsculas: {nome.lower()} ')
print(f'Quantas letras o nome tem: {len(nome.strip())} letras ')
print(f'Quantas letras tem o primeiro nome: {len(tamanho[0])} letras ')
print('Fim!')