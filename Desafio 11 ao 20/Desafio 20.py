# Desafio 20
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
lista_alunos = []

for c in range(0,4):
    nome = str(input('Informe o nome dos alunos: '))
    lista_alunos.append(nome)

shuffle(lista_alunos)
print(f'A sequência das paresentações será: {lista_alunos}')
print(f'Fim!')
