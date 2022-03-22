# Desafio 21
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.


# Desafio 22
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 	o nome com todas as letras maiúsculas;
# 	o nome com todas as letras minúscula;
# 	quantas letras ao todo (sem considerar espaços);
# 	quantas letras tem o primeiro nome.

nome = str(input('Informe o nome completo: '))
tamanho = nome.split()
print(f'Em letras maiúsculas: {nome.upper()} ')
print(f'Em letras minúsculas: {nome.lower()} ')
print(f'Quantas letras o nome tem: {len(nome.strip())} letras ')
print(f'Quantas letras tem o primeiro nome: {len(tamanho[0])} letras ')
print('Fim!')


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


''' Desafio 24
Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome “SANTO” '''





''' Desafio 25
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome. '''


''' Desafio 26
Faça um programa que leia uma frase pelo teclado e mostre:
	quantas vezes apareceu a letra “A”;
	em que posição ela apareceu pela primeira vez;
	em que posição ela apareceu pela última vez.'''


''' Desafio 27
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
	Ex: Ana Maria dos Santos
o	primeiro = Ana
o	ultimo = Santos '''


''' Desafio 28
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O prgrama deverá escrever na tele se o usuário venceu ou perdeu.'''



''' Desafio 29
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80 Km/h mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite. '''



'''Desafio 30
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR. '''