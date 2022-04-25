# Desafio 1
# Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.

nome = str(input('Digite um nome: '))
print(f'Olá {nome}, seja bem vindo!!')


# Desafio 2
# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

nome = str(input('Qual é o seu nome: ')).upper()
dia = int(input('Qual é o dia do seu nascimento: '))
mes = int(input('qual é o mês do seu nascimento: '))
ano = int(input('Qual é o ano do seu nascimento: '))
print(f'Olá, {nome}, você nasceu no dia {dia}/{mes}/{ano}')


# Desafio 3
# Crie um script Python que leia dois números e tente mostrar a soma entre elas.

n1 = int(input('Qual é o primeiro número:'))
n2 = int(input('Qual é o segundo número:'))
soma = n1 + n2
print(f'A soma entre {n1} e {n2} é igual a {soma}')


# Desafio 4
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.


# Desafio 5
# Faça um programa que leia um número inteiro e mostre o seu sucessor e o seu antecessor.

num = int(input('Informe um número para saber seu antecessor e sucessor: '))
print(f'O número sucessor de {num} é {num + 1} e seu antecessor é {num - 1}')

# Desafio 6
# Crie um algoritmo que leia um número e mostre o seu dobro e o seu quadrado.

num = int(input('Informe um número qualquer: '))
print(f'O quadrado do número {num} é {num * num} ')
print(f'O dobro do número {num} é {num * 2} ')

# Desafio 7
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 +n2) / 2
print(f'A média entre as notas {n1} e {n2} é de {media:.2f}')


# Desafio 8
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetro e milímetros.

metro = int(input('informe a medida:'))
print(f'convertendo {metro}m para milímetros -> {metro * 1000}mm')
print(f'convertendo {metro}m para centímetros -> {metro * 100}cm')


# Desafio 9
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número para saber sua tabuada: '))
for contagem in range(1, 11):
    print(f'{num} x {contagem} = {num * contagem}')
print('Fim!')


# Desafio 10
# Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = int(input('Quantos Reais você tem na carteira: R$ '))
dolar = float(input('Informe o valor do dolar na data de hoje: R$ '))
compra = carteira / dolar
print(f'Com R$ {carteira:.2f} na carteira, da para comprar $ {compra:.2f} ')
