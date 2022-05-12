# Desafio 31
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem , cobrando  R$ 0,50 por Km, para viagens até 200 Km e R$ 0,45 para viagens mais longas.

distancia = float(input('Digite uma distância: '))
ate200 = 0.50
acima200 = 0.45
if distancia <= 200:
    print(f'O predo da passagem será: {distancia * ate200:.2f}')
else:
    print(f'O valor será de {distancia * acima200:.2f}')


# Desafio 32
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite um ano qualquer: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO é BISSEXTO!')


# Desafio 33
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o Primeiro número: '))
n2 = int(input('Digite o Segundo número: '))
n3 = int(input('Digite o terceiro número: '))
#Verificando qual é o maior valor:
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
#Verificando qual é o menor valor:
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O MAIOR número entre os três é o {maior}')
print(f'O MENOR número entre os três é o {menor}')


# Desafio 34
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o salário do funcionário: R$ '))
if salario <= 1250.00:
    novo = salario * 1.15
else:
    novo = salario * 1.10
print(f'Quem ganhava R$ {salario:.2f} passa a ganhar R$ {novo:.2f}')


# Desafio 35
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Seguimento A: '))
r2 = float(input('Seguimento B: '))
r3 = float(input('Seguimento C: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR um triâgulo!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triâgulo!')

#
# Desafio 36
# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

imovel = float(input('Valor do imóvel: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento: '))
prestação = imovel / (anos * 12)
mínimo = salario * 0.30
print(f'Para pagar um imovél de R$ {imovel:.2f} em {anos} anos', end='')
print(f'O valor das pretações será de R$ {prestação:.2f}')

if prestação <= mínimo:
    print('O seu financiamento foi \033[1;33mAPROVADO!')
else:
    print(f'Seu finanaciamento foi \033[1;31mNEGADO!')


# Desafio 37
# Desenvolva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão:
# 	1 para binário
# 	2 para octal
# 	3 para hexadecimal

numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}')
elif opção == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif opção == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('Opção inválida. Tente novamente.')

# Desafio 38
# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# 	O primeiro valor é maior
# 	O segundo valor é maior
# 	Não existe valor maior, os dois são iguais

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('O \033[1;31mPRIMEIRO\033[m valor é o maior. ')
elif n2 > n1:
    print('O \033[1;32mSEGUNDO\033[m valor é o maior.')
else:
    print('\033[1;35mOs DOIS valores são iguais!')


# Desafio 39
# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade:
# 	Se ele ainda vai se alistar ao serviço militar.
# 	Se é a hora de alistar.
# 	Se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Você tem de se alistar \033[1;31mIMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
elif idade > 18:
    saldo = idade - 18
    print(f'\033[1;31mVocê deveria ter se alistado há {saldo} anos! ')


# Desafio 40
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# 	Média abaixo de 5,0: Reprovado    Média entre 5,0 e 6,9: Recuperação   Média 7,0 ou superior: Aprovado

nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
média = (nota1 + nota2) / 2
if 7 > média >= 5:
    print(f'Sua média foi {média:.1f}')
    print('Você está em RECUPERAÇÃO!')
elif média < 5:
    print(f'Sua média foi {média:.1f}')
    print('Você foi REPROVADO!')
else:
    print(f'Sua média foi {média:.1f}')
    print('Parabéns, você foi APROVADO!')
