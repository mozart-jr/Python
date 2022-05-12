# Desafio 51
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos desta razão.
# PA  Progressão Aritmética


primeiro = int(input('Informe o Primeiro Termo: '))
razao = int(input('Informe a Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f' {c} ', end='-> ')
print(('ACABOU!'))


# Desafio 52
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Escolha um número: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[1;34m', end=' ')
        total = total + 1
    else:
        print('\033[1;33m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[m O número {numero} foi divisível {total} vezes')
if total == 2:
    print(f'O número {numero} é primo!')
else:
    print(f'O número {numero} não é primo!')


# Desafio 53
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Palíndromo  frase que pode ser lida de traz para frente, com o mesmo significado.
# Ex: APÓS A SOPA
#        A SACADA DA CASA
#        A TORRE DA DERROTA
#        O LOBO AMO O BOLO
#        ANOTARAM A DATA DA MARATONA


frase = str(input('Digite uma frase para saber se ela é Palíndromo: ')).strip().lower()
lista_palavras = frase.split()
print(f'{lista_palavras}')

junto = ''.join(lista_palavras)
print(f'{junto}')

inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]

print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('É Palíndrmo! ')
else:
    print('Não é Palíndromo! ')

# Desafio 54
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.


from datetime import date

atual = date.today().year
adulto = 0
crianca = 0
for pessoas in range(1, 8):
    nasc = int(input(f'Qual o ano de nascimento da {pessoas}ª pessoa: '))
    idade = atual - nasc
    if idade >= 21:
        adulto = adulto + 1
    else:
        crianca = crianca + 1
print(f'Ao todos tivemos {adulto} pessoas maiores de idade')
print(f'Ao todos tivemos {crianca} pessoas menores de idade')

# Desafio 55
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


maior = 0
menor = 0
for p in range(1, 6):
    # p-> peso
    peso = float(input(f'Informe o {p}º peso: '))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi de {maior:.2f} kg')
print(f'O menor peso foi de {menor:.2f}kg')

# Desafio 56
# Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas, no final do programa mostre:
# •	A média de idade do grupo;
# •	Qual é o nome do homem mais velho;
# •	Quantas mulheres tem menos de 20 anos.


somaidade = 0
mediaidade = 0
maior_idade_homem = 0
homem_mais_velho = ''
tot_mulher_20 = 0
cont = 0

for pessoa in range(1, 5):
    cont = cont + 1
    print(f'{pessoa}º nome: ')
    nome = str(input('Nome: ')).strip()

    idade = int(input(f'Idade: '))

    sexo = str(input(f'Sexo: [M/F]: ')).strip()
    somaidade = somaidade + idade

    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        homem_mais_velho = nome

    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_mais_velho = nome

    if sexo in 'Ff' and idade < 20:
        tot_mulher_20 = tot_mulher_20 + 1
mediaidade = somaidade / cont

print(f'A média de idade do grupo é de {mediaidade} anos. ')
print(f'O Homem mais velho tem {maior_idade_homem} anos e se chama {homem_mais_velho} ')
print(f'Ao todo são {tot_mulher_20} mulher(es) com menos de 20 anos. ')
Curso
Python  # 14 – Laços de repetição (Parte 2)

# Desafio 57
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

# .upper()[0] -> pega só a primeira letra.

sexo = str(input('informe seu sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFm':
    sexo = str(input('Dados inválidos. por favor, informe seu sexo:  ')).strip().upper()[0]
print(f'sexo {sexo} registrado com sucesso!')


# Desafio 58
# Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar até adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue  adivinhar qual foi? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Escolha um número: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente outra vez! ')
        elif jogador > computador:
            print('Menos... Tente outra vez! ')
print(f'Acertou com {palpite} tentativas... Parabéns!! ')

# Desafio 59
# Crie um programa que leia dois valores e mostre um menu na tela.
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.


n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''Selecione uma das opções abaixo: 
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual foi a sua escolha: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é igual a {soma}')

    elif opcao == 2:
        multiplicao = n1 * n2
        print(f' {n1} * {n2} = {multiplicao} ')

    elif opcao == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}')
        elif n1 == n2:
            print('Os valores são iguais')
        else:
            print(f'O maior valor é {n2}')

    elif opcao == 4:
        print('informe os números novamente. ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Encerrando...')

    else:
        print('Opção Inváida. Tente novamente.')
        print('=-=' * 10)
print('Fim do programa! Volte sempre!')

# Desafio
# 60
# Faça um programa que leia um número qualquer e leia seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial
numero = int(input('Digite um número para calcular o seu Fatorial: '))
f = factorial(numero)
print(f'O Fatorial de {numero} é {f}')
print('FIM')

###############################  ou  ############################

numero = int(input('Digite um número para calcular o seu Fatorial: '))
c = numero
fatorial = 1
print(f'calculando {numero}! = ')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial = fatorial * c
    c = c - 1
print(f'{fatorial}')
print('FIM'
