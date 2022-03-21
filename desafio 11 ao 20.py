''' Desafio 11
Faça um programa que leia a largura e a altura de uma parede em metros quadrados, calcule a sua área,
e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m². '''

largura = float(input('Informe a largura: '))
altura = float(input('Informe a altura: '))
area = largura * altura
print(f'esta parede tem {area}m²')
print(f'Precisará de {area / 2} latas de tinta ')
print('Fim! ')

''' Desafio 12
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. '''

# produto = str(input('nome do produto:')).upper()
# preco_normal = float(input('Preço: '))
# desconto = 0.95
# print(f'O preço desse produto com 5% de desconto é {preco_normal * desconto}')
# print('FIM!!')


''' Desafio 13
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. '''

# salario = float(input('Qual é o salário: R$ '))
# aumento = 1.15
# novo_salario = salario * aumento
# print(f'O valor do novo salário é de R$ {novo_salario:.2f}')
# print('FIM!')


''' Desafio 16
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6 '''
## tunch -> descarta os valoeres depois da vírgula
## precisa importar da biblioteca math

# from math import trunc
# num = float(input('Informe um número Real: '))
# print(f'A porção inteira do número Real {num} é {trunc(num)}')
# print('Fim!')

################################## ###### ou #############################################

# from math import trunc
# num = float(input('Digite um número REAL: '))
# print(f'O valor inteiro do número {num} é {trunc(num)}')
# print('FIM !!')


''' Desafio 17
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.
Obs: hypot  é para calcular a hipotenusa.'''

#formula da Hipotenusa -> H² = Co² + Ca²
#Raiz quadrada = (1/2)
#H = (co² + ca²) ** (1/2)
# co = float(input('Informe o valor do cateto oposto: '))
# ca = float(input('Informe o valor do cateto adjacente: '))
# h = (co**2 + ca**2) ** (1/2)
# print(f'O valor da hipotenusa é {h:.2f}')

################################## ###### ou #############################################

# from math import hypot
# co = float(input('Informe o valor do cateto oposto: '))
# ca = float(input('Informe o valor do cateto adjacente: '))
# print(f'O valor da hipotenusa é {hypot(co, ca):.2f}!')

################################## ###### ou #############################################

# co = int(input('Informe o comprimento do Cateto Oposto ao ângulo: '))
# ca = int(input('Informe o comprimento do Cateto Adjacente ao ângulo: '))
# hyp = (co ** 2 + ca ** 2) ** (1/2)
# print(f'A Hypotenusa é {hyp}')
# print('FIM !!')


''' Desafio 18
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e a tangente desse ângulo.'''

# import math
# ang = int(input('Informe o ângulo: '))
# sen = math.sin(math.radians(ang))
# cos = math.cos(math.radians(ang))
# tang = math.tan(math.radians(ang))
# print(f'O Seno {sen:.3f}')
# print(f'O Cosseno {cos:.3f}')
# print(f'A Tangente {tang:.3f}')
# print('FIM !!')


''' Desafio 19
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faço um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido. '''

# from random import choice
# a1 = str(input('Nome do primeiro aluno: ')).upper()
# a2 = str(input('Nome do segundo aluno: ')).upper()
# a3 = str(input('Nome do terceiro aluno: ')).upper()
# a4 = str(input('Nome do quarto aluno: ')).upper()
# lista = (a1, a2, a3, a4)
# sorteio = choice(lista)
# print(f'O aluno sorteado para apagar o quadro foi: {sorteio}')

#########################  ou  ###########################

# from random import choice
# lista_alunos = []
# n = int(input('Informe o n de alunos: '))
#
# for _ in range(0, n):
#     alunos = str(input('Informe o nome do aluno: '))
#     lista_alunos.append(alunos)                       # append() -> adiciona na lista
#
# print(f'o aluno é: {choice(lista_alunos).upper()}')

###################################  ou  #################################

# from random import choice
# lista_alunos = []
#
# for _ in range(0, 4):
#     alunos = str(input('Informe o nome do aluno: '))
#     lista_alunos.append(alunos)
#
# print(f'o aluno é: {choice(lista_alunos).upper()}')



# from random import choice             ##############  choice -> aleatório  #################
# lista_de_alunos = []
# n = int(input('Informe a quantidde de alunos para o sorteio: '))
# for c in range(0, n):
#     alunos = str(input('Informe o nome do aluno: '))
#     lista_de_alunos.append(alunos)
#
# print(f'O aluno sorteado foi: {choice(lista_de_alunos).upper()}')
# print('FIM !!')


''' Desafio 20
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. '''

# from random import shuffle
# lista_alunos = []
#
# for c in range(0,4):
#     nome = str(input('Informe o nome dos alunos: '))
#     lista_alunos.append(nome)
#
# shuffle(lista_alunos)
# print(f'A sequência das paresentações será: {lista_alunos}')
# print(f'Fim!')

