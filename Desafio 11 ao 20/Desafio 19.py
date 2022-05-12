
# Desafio 19
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faço um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice
a1 = str(input('Nome do primeiro aluno: ')).upper()
a2 = str(input('Nome do segundo aluno: ')).upper()
a3 = str(input('Nome do terceiro aluno: ')).upper()
a4 = str(input('Nome do quarto aluno: ')).upper()
lista = (a1, a2, a3, a4)
sorteio = choice(lista)
print(f'O aluno sorteado para apagar o quadro foi: {sorteio}')

#########################  ou  ###########################

from random import choice
lista_alunos = []
n = int(input('Informe o n de alunos: '))

for _ in range(0, n):
    alunos = str(input('Informe o nome do aluno: '))
    lista_alunos.append(alunos)                       # append() -> adiciona na lista

print(f'o aluno é: {choice(lista_alunos).upper()}')

###################################  ou  #################################

from random import choice
lista_alunos = []

for _ in range(0, 4):
    alunos = str(input('Informe o nome do aluno: '))
    lista_alunos.append(alunos)

print(f'o aluno é: {choice(lista_alunos).upper()}')


from random import choice             ##############  choice -> aleatório  #################
lista_de_alunos = []
n = int(input('Informe a quantidde de alunos para o sorteio: '))
for c in range(0, n):
    alunos = str(input('Informe o nome do aluno: '))
    lista_de_alunos.append(alunos)

print(f'O aluno sorteado foi: {choice(lista_de_alunos).upper()}')
print('FIM !!')