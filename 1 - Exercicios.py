# exercicio teste de while:

# numero = 0
# soma = 0
# while numero != 999:
#     numero = int(input('Digite um número:'))
#     soma = soma + numero
#
# print(f'A soma dos numeros digitasoe é {soma}')
# print('Fim!')

# numero = 0
# soma = 0
# while True:
#     numero = int(input('Digite um número:'))
#     if numero == 999:
#         break
#     soma = soma + numero
#
# print(f'A soma dos numeros digitasoe é {soma}')
# print('Fim!')

#-----------------------------  Inicio dos Desafios   ----------------------------

# print('Desafio 1')
# nome = str(input('Digite um nome:'))
# print(f'Olá {nome}, seja bem vindo!')
# print('Fim!')

# print('Desafio 2')
# nome = str(input('Digite o nome: '))
# dia = int(input('Digita o dia: '))
# mes = int(input('Digita o mês: '))
# ano = int(input('Digite o ano: '))
# print(f'{nome} nasceu no dia {dia}/{mes}/{ano}')
# print('Fim!')

# print('Desafio 6')
# n1 = int(input('Qual é o 1º número: '))
# n2 = int(input('Qual é o 2º número: '))
# soma = n1 + n2
# print(f'A soma entre os números {n1} e {n2} é {soma}')
# print('Fim!')

# print('Desafio 6')
# num = int(input('Digite um número para saber seu dobro e seu quadrado: '))
# dobro = num * 2
# quad = num * num
# print(f'O Dobro do número {num} é {dobro} e o seu quandrado é {quad}')
# print('Fim!')

# print('Desafio 7')
# n1 = int(input('Informe a primeira nota: '))
# n2 = int(input('Informe a segunda nota: '))
# media = (n1 + n2) / 2
# print(f'Sua média foi {media:.2f}:')
# print('Fim!')

# print('Desafio 8')
# medida = int(input('Informe um valor em metros(m): '))
# cent = medida * 100
# milim = medida * 1000
# print(f'O valor em centímetros é de {cent}cm')
# print(f'O valor em milímetros é de {milim}mm')
# print('Fim!')

# print('Desafio 9')
# num = int(input('Digite um número para saber sua tabuada: '))
# print(f'A tabuado do número {num} é: ')
# for contagem in range(1, 11):
#         print(f'{num} x {contagem} = {num * contagem}')
# print('Fim!')

# print('Desafio 10')
# carteira = int(input('Quantos Reais você tem na carteira: R$ '))
# dollar = float(input('Qual a cotação do dolar hoje: R$ '))
# conversao = carteira / dollar
# print(f'Com R$ {carteira} na carteira você pode comprar $ {conversao:.2f}')
# print('Fim!')

# print('Desafio 11')
# largura = int(input('Informe a largura da parede(m): '))
# altura = int(input('Informe a altura da parede(m): '))
# area = largura * altura
# rendimento = int(input('Informe o rendimento (em litros) por lata: '))
# print(f'A área desta parede é de {area}m²')
# print(input(f'Com um rendimento de {rendimento}l por lata você precisará de {area / rendimento} latas'))
# print('Fim!')

# print('Desafio 12')
# produto = str(input('Qual é o produto: '))
# preco = int(input('Informe o preço do produto: R$ '))
# desconto = 0.05
# print(f'O preço com desconto de 5% é de R$ {(preco - desconto):.2f} ')
# print(f'o desconto foi de R$ {(preco *desconto):.2f}')
# print('Fim!')

# print('Desafio 13')
# nome = str(input('informe o nome do funcionário: '))
# salario = float(input('informe o saláio: R$ '))
# aumento = 0.15
# print(f'O(A) funcionário(a) {nome.capitalize()} teve um aumento salarial de {(aumento * 100):.2f}% ')
# print(f'O salário foi de R$ {salario:.2f} para {(salario * 1.15):.2f}')
# print('Fim!')

# print('Desafio 16')
# num = float(input('Digite um número Real: '))
# print(f'A parte inteira do número {num} é o número {num.__trunc__()}')
# print('Fim!')

# print('Desafio 17')
# co = int(input('Informe o comprimento do cateto oposto: '))
# ca = int(input('Informe o comprimento do cateto adjacente: '))
# hyp = (co ** 2 + ca ** 2) ** (1/2)
# print(f'A hipotenusa é {hyp:.2f}')
# print('Fim!')

# print('Desafio 18')
# import math
# ang = float(input('Informe o ângulo: '))
# seno = math.sin(math.radians(ang))
# cosseno = math.cos(math.radians(ang))
# tangente = math.tan(math.radians(ang))
# print(f'-> {seno:.4f} -> {cosseno:.4f} -> {tangente:.4f}')
# print('Fim!')

# print('Desafio 19')
# from random import choice
# lista_de_alunos = []
#
# for c in range(1, 5):
#     alunos = str(input('Informe o nome dos alunos: '))
#     lista_de_alunos.append(alunos)
#
# sorteio = choice(lista_de_alunos)
# print(f'O aluno selecionado foi: {choice(lista_de_alunos).upper()}')
# print('Fim!')

# print('Desafio 20')
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

# print('Desafio 22')
# nome = str(input('Informe o nome completo: '))
# tamanho = nome.split()
# print(f'Com letras maiúsculas: {nome.upper()} ')
# print(f'Com letras minúsculas: {nome.lower()} ')
# print(f'Quantas letras tem o nome completo, sem espaços: {len(nome.strip())} letras ')
# print(f'O primeiro nome tem {len(tamanho[0])} letras')
# print('Fim!')

# print('Desafio 23')
# num = int(input('Digite um número entre 0 e 9999: '))
# unidade = num // 1 % 10
# dezena = num // 10 % 10
# centena = num // 100 % 10
# milhar = num // 1000 % 10
# print(f'Unidade: {unidade}')
# print(f'Dezena {dezena}')
# print(f'Centena {centena}')
# print(f'Milhar {milhar}')
# print('Fim!')

# print('Desafio 24')
# cidade = str(input('Digite o nome da cidade: ')).strip().upper()
# soma_das_letras = ''
#
# for index, c in enumerate(cidade):
#     if index == 0 and c == 'S':               # index -> é a posição da lista(S = O)
#         soma_das_letras += c
#     if index == 1 and c == 'A':
#         soma_das_letras += c
#     if index == 2 and c == 'N':
#         soma_das_letras += c
#     if index == 3 and c == 'T':
#         soma_das_letras += c
#     if index == 4 and c == 'O':
#         soma_das_letras += c
#
# if soma_das_letras == 'SANTO':
#     print(f'Esta cidade começa com a palavra "SANTO" ')
# else:
#     print(F'Esta cidade NÃO começa com o nome "SANTO "')
# print('Fim!')

###################################  ou o pedido no exercício  #################################

# cidade = str(input('Digigte o nome da cidade: ')).strip().upper()
# print(cidade[:5] == 'SANTO')
# print('Fim!')


# print('Desafio 25')
# nome = str(input('Digite o nome: ')).strip().capitalize()
# print(f'Silva' in nome)
# print('Fim!')


# print('Desafio 26')
# frase = str(input('Digite uma frase: ')).strip().upper()
# print(f'A letra "A" apareceu na frase "{frase}" {frase.count("A")} vezes ')
# print(f'a primeira vez que a letra "A" foi na posição {frase.find("A")}')
# print(f'A letra "A" apareceu pela ultima vez na posição {frase.rfind("A")}')
# print('Fim!')

# print('Desafio 27')
# nome = str(input('Informe o nome completo: ')).upper().strip().split()
# print(f'O primeiro nome é {nome[0]}')
# print(f'O ultimo nome é {nome[-1]}')
# print('Fim!')

# print('Desafio 28')
# from random import randint
# computador = randint(0, 5)
# jogador = int(input('Digite um número entre 0 e 5: '))
# if jogador == computador:
#     print('Parabéns! Você escolheu o mesmo número que o computador!')
#     print(f'O computador jogou {computador} e você escolheu {jogador}')
# else:
#     print('Que pena, você errou!')
#     print(f'O computador jogou {computador} e você escolheu {jogador}')
# print('Fim!')

# print('Desafio 29')
# print('VELOCIDADE MÁXIMA PERMITIDA = 80 Km/h')
# velocidade = int(input('Em qual velocidade o motorista passou naquele trecho: '))
# multa = 7
# if velocidade <= 80:
#     print(f'Boa Viagem!')
# else:
#     print(f'MULTADO! Você passou acima da velocidade máxima permitida!')
#     print(f'Sua multa é de R$ {(velocidade - 80 ) * multa:.2f}')
# print('Fim!')

# print('Desafio 30')
# num = int(input('Digite um número para saber se é Par ou Ímpar: '))
# divisao = num % 2
# if divisao == 0:
#     print(f'O número {num} é PAR!')
# else:
#     print(f'O número {num} é ÍMPAR!')
# print('Fim!')

# print('Desafio 31')
# distancia = int(input('Informe a distância da sua viagem: '))
# ate200 = 0.50
# acimade200 = 0.45
# if distancia <= 200:
#     print(f'O valor da sua viagem é de R$ {distancia * ate200:.2f} ')
# else:
#     print(f'O valor da sua viagem será de R$ {distancia * acimade200:.2f} ')
# print('Boa Viagem!')
# print('Fim!')

# print('Desafio 32')
# # divisivel por 4, por 100 e por 400
# ano = int(input('Informe o ano para saber se ele é bissexto: '))
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print(f'O ano de {ano} é um ano bissexto!')
# else:
#     print(f'O ano de {ano} não é bissexto! ')
# print('Fim!')

# print('Desafio 33')
# print('Digite 3 números para saber qual é o maior e qual é o menor:')
# n1 = int(input('1º número: '))
# n2 = int(input('2º número: '))
# n3 = int(input('3º número: '))
#
# if n1 > n2 and n1 > n3:
#     print(f'O número {n1} é o maior.')
# if n2 > n1 and n2 > n3:
#     print(f'O número {n2} é o maior.')
# if n3 > n1 and n3 > n2:
#     print(f'O número {n3} é o maior.')
#
# if n1 < n2 and n1 < n3:
#     print(f'O número {n1} é o menor.')
# if n2 < n1 and n2 < n3:
#     print(f'O número {n2} é o menor.')
# if n3 < n1 and n3 < n2:
#     print(f'O número {n3} é o menor.')
# print('Fim!')

# print('Desafio 34')
# salario = float(input('Qual é o salario: R$ '))
# acima_de_1250 = 1.10
# abaixo_de_1250 = 1.15
# if salario >= 1250:
#     print('O aumento foi de 10% ')
#     print(f'O salario foi de R$ {salario:.2f} para R$ {salario * acima_de_1250:.2f}')
# else:
#     print('O aumento foi de 15% ')
#     print(f'O salario foi de R$ {salario:.2f} para R$ {salario * abaixo_de_1250:.2f}')
# print('Fim!')

# print('Desafio 35')
# # Se a soma entre os dois lados menores for maior que o terceiro lado é possível formar um triângulo.
# print('informe 3 medidas para saber se é possível criar um triâmgulo: ')
# reta_1 = int(input('Reta A -> '))
# reta_2 = int(input('Reta B -> '))
# reta_3 = int(input('Reta C -> '))
# if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_2 + reta_1:
#     print(f'É possível criar um Triângulo!')
# else:
#     print(f'Não é possível crias um Triângulo! ')
# print('Fim! ')

# print('Desafio 36')
# imovel = float(input('Informe o valor do imóvel: R$ '))
# salario = float(input('qual é o salário:  R$ '))
# tempo_de_financiamento = int(input('Em quantos anos será o financiamento: '))
# prestacao = imovel / (tempo_de_financiamento * 12)
# limite_salario = salario * 0.30
#
# print(f'Para financiar um imóvel de R$ {imovel:.2f} em {tempo_de_financiamento} anos')
# print(f'O valor da prestação será de R$ {prestacao:.2f} ')
#
# if prestacao <= limite_salario:
#     print(f'Financiamnto \033[1;33mAPROVADO!')
# else:
#     print('Financiamento \033[1;31mNEGADO!')
# print('Fim!')

# print('Desafio 37')
# numero = int(input('Digite um número inteiro: '))
# print('''Escolha uma das bases para conversão:
# [ 1 ] Converte para Binário
# [ 2 ] Converte para Octal
# [ 3 ] Converte para Hexadecimal''')
#
# opcao = int(input('Escolha uma das três opções: '))
# if opcao == 1:
#     print(f'{numero} Convertido para Binário é igual a {bin(numero)}')
# elif opcao == 2:
#     print(f'{numero} Convertido parar Octal é igual a {oct(numero)}')
# elif opcao == 3:
#         print(f'{numero} Convertido para Hexadecimal é igual a {hex(numero)}')
# else:
#     print('Opção inválida. Tente novamente.')
# print('Fim!')

# print('Desafio 38')
# n1 = int(input('Primeiro Número: '))
# n2 = int(input('Segundo Número: '))
#
# if n1 > n2:
#     print(f'O Primeiro valor ({n1}) é maior. ')
# elif n2 > n1:
#     print(f'O Segundo valor ({n2}) é o maior. ')
# else:
#     print(f'Os dois Números são iguais! ')
# print('Fim!')

# print('Desafio 39')
# from datetime import date
# data_atual = date.today().year
# nascimento = int(input('Qual é ano de nescimento: '))
# idade = data_atual - nascimento
# if idade == 18:
#     print(f'Você deve se alistar este ano sem falta!!')
# elif idade < 18:
#     print('Você está abaixo da idade de 18 anos, não precisa se alistar este ano.')
# else:
#     print('Você passou do tempo do alistamento!! ')
# print('Fim!')

# print('Desafio 40')
# nota1 = float(input('1ª Nota: '))
# nota2 = float(input('2ª Nota: '))
# media = (nota1 + nota2) / 2
# if media < 5:
#     print('REPROVADO!')
# elif media >= 5 and media < 7:
#     print('RECUPERAÇÃO')
# else:
#     print('APROVADO!')
# print('Fim!')

# print('Desafio 41')
# from datetime import date
# ano_atual = date.today().year
# nome = str(input('Informe o nome do atleta:'))
# ano_nascimento = (int(input('Informe o Ano de Nascimento: ')))
# idade = ano_atual - ano_nascimento
#
# print(f'O atleta {nome.upper()} tem {idade} anos.')
# if idade <= 9:
#     print('Categoria Mirim')
# elif idade > 9 and idade < 14:
#     print('categoria Infantil')
# elif idade > 14 and idade < 19:
#     print('categoria Junior')
# elif idade > 19 and idade < 25:
#     print('categoria Sênior')
# elif idade >= 25:
#     print('Categoria Master')
#
# print('Fim!')

# print('Desafio 42')
# r1 = float(input('Seguimento 1: '))
# r2 = float(input('Seguiment0 2: '))
# r3 = float(input('Seguimento 3: '))
#
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print('Com estas medidas é possível criar um triângulo: ', end='')
#     if r1 == r2 == r3:
#         print('EQUILÁTERO')
#     elif r1 != r2 != r3 != r1:
#         print('ESCALENO')
#     else:
#         print('ISÓSCELES')
# else:
#     print('não é possível criar um triângulo com estes valores')
#
# print('Fim!')

# print('Desafio 43')
# peso = float(input('Peso (kg): '))
# altura = float(input('Altura (m): '))
# imc = peso / (altura) ** 2
# print(f'Seu imc é de {imc:.2f}')
# if imc < 18.5:
#         print('Até 18.5:  Abaixo do Peso. ')
# elif imc >= 18.5 and imc < 25:
#     print('Entre 18.5 e 25: Peso Ideal. ')
# elif imc >= 25 and imc < 30:
#     print('Entre 25 e 30: Sobrepeso. ')
# elif imc >= 30 and imc < 40:
#     print('entre 30 e 40: Obesidade. ')
# else:
#     print('Acime de 40: Obesidade Mórbida. ')
# print('Fim!')

# print('Desafio 44')
# preco_total = float(input('Valor Total da compra: R$ '))
# print('''Escolha a Forma de Pagamento:
#     [1] Á Vista dinheiro/cheque -> Desconto de 10%
#     [2] Á vista no Cartão -> Desconto de 5%
#     [3] 2x no Cartão - Sem Desconto
#     [4] 3x ou mais no Cartão - Juros de 20%''')
# opcao = int(input('Digite a opção: '))
# total = preco_total
#
# if opcao == 1:
#     print(f'R$ {total * 0.9:.2f} ')
# elif opcao == 2:
#     print(f'R$ {total * 0.95:.2f} ')
# elif opcao == 3:
#     print(f'R$ {total:.2f} ')
# elif opcao == 4:
#     print(f'R$ {total * 1.20:.2f} ')
#     quantidade_de_parcelas = int(input('Em quantas vezes: '))
#     print(f'Sua compra será parcelada em {quantidade_de_parcelas}x de R$ {total / quantidade_de_parcelas:.2f}')
#
# print('Fim!')

# print('Desafio 45')
# from random import randint
# escolha = ['Pedra', 'Papel', 'Tesoura']
# computador = randint(0, 2)
#
# print('''Escolha:
# [1] -> Pedra
# [2] -> Papel
# [3] -> Tesoura''')
#
# # as opcoes 1, 2 e 3, em uma lista se tornam 0, 1 e 2 respectivamente
#
# # opcao que o jogador escolher - 1 (o jogador nao sabe que listas começam do 0)
# jogador = int(input('Qual você escolhe: '))-1
#
# print(f'Você jogou {escolha[jogador]}')
# print(f'Computador jogou {escolha[computador]}.')
#
# #Jogador - Pedra
# if jogador == 0 and computador == 1:
#     print('Você Perdeu!')
# elif jogador == 0 and computador == 2:
#     print('Você Venceu!')
#
# #Jogador - Papel
# elif jogador == 1 and computador == 0:
#     print('Você Venceu!')
# elif jogador == 1 and computador == 2:
#     print('Você Perdeu!')
#
# #Jogador - Tesoura
# elif jogador == 2 and computador == 1:
#     print('Você Perdeu!')
# elif jogador == 0 and computador == 2:
#     print('Você Venceu!')
#
# else:
#     print('EMPATE! Jogue novamente!')
#
# print('Fim!')

# print('Desafio 46')
# from time import sleep
# for contagem in range(10, -1, -1):
#     print(contagem)
#     sleep(1.0)
# print('Feliz ano novo!!!')
# print('Fim!')

# print('Desafio 47')
# print('Mostrar os números apres entre 1 e 50 ')
# for numero in range(1, 51):
#     if numero % 2 == 0:
#         print(numero)
# print('Fim!')

# print('Desafio 48')
# print('Qual é a soma entre todos os números -> ÍMPARES" <- que são múltiplos de 3 e estão entre 1 e 500? ')
# contador = 0
# soma = 0
# print('O números múltiplos de três entre 1 e 500 são:')
# for multiplo_de_tres in range(1, 501, 2):
#     if multiplo_de_tres % 3 == 0:
#         print(multiplo_de_tres)
#         contador += 1
#         soma += multiplo_de_tres
# print(f'A soma entre os {contador} números ímpares e múltiplos de 3, entre 1 e 500 é: {soma}')
# print('Fim!')

# print('Desafio 49')
# numero = int(input('Digite um número para saber sua tabuada:'))
# for num in range(1, 11):
#     print(f'{numero} x {num} = {numero * num}')
# print('Fim!')

# print('Desafio 50')
# soma = 0
# contador = 0
#
# for c in range(1, 7):
#     numero = int(input(f'Digite o {c}º número:'))
#
#     if numero % 2 == 0:
#         soma += numero
#         contador += 0
#
# print(f'A sodos dos números pares é: {soma}')
# print('Fim!')


# print('Desafio 51')
# print('10 TERMOS DE UMA PRESSÃO ARITIMÉTICA:')
# an = enésimo termo
# a1 = primeiro termo
# n = número de termos
# r= razão
# print('an = a1 + (n – 1) * r')
#
# primeiro = int(input('Primeiro Termo: '))
# razao = int(input('Razão: '))
# decimo_termo = primeiro + (10 - 1) * razao
# for c in range(primeiro, decimo_termo + razao, razao):
#     print(f'{c}', end=' -> ')
# print('Fim!')

# print('Desafio 52')
# numero = int(input('Digite um número para saber se é PRIMO: '))
# contador = 0
#
# for numero_primo in range(1, numero + 1):    # (numero + 1) é o número que foi digitado
#     if numero % numero_primo == 0:
#         print('\033[1;34m', end='')
#         contador += 1
#     else:
#         print('\033[1;33m', end='')
#         print(f'{numero_primo} ', end='')
# print(f'\n\033[mO número {numero} foi divisivel {contador} vezes.')

# if contador == 2:    # == 2 porque só é primo se for divisível por 1 e por ele meso
#     print(f'O número {numero} É PRIMO. ')
# else:
#     print(f'o número {numero} NÃO É PRIMO. ')
#
# print('Fim!')

# print('Desafio 53')
#strip() -> remove os espaços entre as frases, no começo e no fim.
#lower() -> deixa toda as letras minúsculas.
#split() -> divide as palavras e transforma em lista
#join() -> junta todas as palavras
#len() -> vai contar quantas letras tem a frase

#Separando as palavras da frase.
# frase = str(input('Digite uma frase para saber se ela é POLÍNDROMO: ')).strip().lower()
# lista_de_palavras = frase.split()
# print(f'{lista_de_palavras}')
#
# #Juntando as palavras da frase, sem espaço.
# juntar_as_palavras = ''.join(lista_de_palavras)
# print(f'{juntar_as_palavras}')
#
# frase_inversa = ''
#
# for letra in range(len(frase_inversa) -1, -1, -1):
#     frase_inversa = frase_inversa + juntar_as_palavras[letra]
# print(f'o inverso de {juntar_as_palavras} é {frase_inversa}')
# if juntar_as_palavras == frase_inversa:
#     print('É PALÍNDROMO!')
# else:
#     print('Não é PALÍNDROMO!')
#
# print('Fim!')

# print('Desafio 54')
#
# from datetime import date
# data_atual = date.today().year
# maior_18 = 0
# menor_18 = 0
#
# for pessoas in range(1, 8):
#     nascimento = int(input(f'Informe o ano de nascimento da {pessoas}ª pessoa: '))
#     idade = data_atual - nascimento
#     if idade >= 18:
#         maior_18 += 1
#
#     else:
#         menor_18 += 1
# print(f'Destas sete pessoas, {maior_18} são maiores de 18 anos e {menor_18} são menores de 18 anos.')

# print('Desafio 55')
#
# lista_pesos = []
# for pessoas in range(1, 6):
#     peso = float(input(f'informe o peso da {pessoas}ª pessoa: '))
#     lista_pesos += [peso]
#
# # print('')
# print(f'O maior peso foi:', max(lista_pesos))
# print(f'O menor peso foi:', min(lista_pesos))
#
# print('Fim!')

# print('Desafio 56')
#
# idade_h_mais_velho = 0
# cont = 0
# media = 0
# for pessoas in range(1, 5):
#     print(f'----{pessoas}ª PESSOA----')
#
#     nome = str(input('Nome: ')).strip().capitalize()
#     idade = int(input('Idade: '))
#     sexo = str(input('M/F: ')).strip().upper()
#
#     if sexo == 'M':
#         if idade > idade_h_mais_velho:
#             idade_h_mais_velho = idade
#             nome_homem_mais_velho = nome
#
#     if sexo == 'F':
#         if idade < 21:
#             cont = cont + 1
#     media += idade
#
# media_final = media / 4
# print(f'A média de idade do grupo é {media_final}.')
# print(f'O homem mais velho é {nome_homem_mais_velho}, de {idade_h_mais_velho} anos.')
# print(f'Há {cont} mulheres com menos de 20 anos.')
#
# print('Fim!')

# print('Desafio 57')
#
# sexo = str(input('Informe o sexo: [M/F]:')).upper()
# if sexo == 'M':
#     print('Sexo masculino. ')
# elif sexo == 'F':
#     print('Sexo Feminino. ')
# else:
#     print('Dados inválidos! Digite novamente:')
#
# print('Fim!')


# print('Desafio 58')
#
# from random import randint
# computador = randint(0, 11)
#
# tentativas = 0
# acertou = False

# print('Tente a certar o mesmo número que o computador.')
#
# while not acertou:
#     jogador = int(input('Digite um número entre 0 e 10: '))
#     tentativas += 1
#
#     if jogador == computador:
#         acertou = True
#
#     else:
#         if jogador < computador:
#             print('Você errou! Escolha um número MAIOR!')
#         elif jogador > computador:
#             print('Você errou! Escolhou um número MENOR!')
#
# print(f'Parabéns! Você e o computador escolheram o número {jogador}')
# print(f'Você fez {tentativas} tentativas. ')
#
# print('Fim!')


# print('Desafio 59')
#
# n1 = int(input('Primeiro número: '))
# n2 = int(input('Segundo número: '))
#
# opcao = 0
#
# while opcao != 5:
#     print('''Escolha uma das opções abaixo:
#     [1] -> Somar
#     [2] -> Multiplicar
#     [3] -> Maior número
#     [4] -> Novos números
#     [5] -> Sair do Programa''')
#
#     opcao = int(input('Qual opção a sua escolha: '))
#
#     if opcao == 1:
#         print(f'A soma entre {n1} + {n2} = {n1 + n2}. ')
#
#     elif opcao == 2:
#         print(f'A multiplicação entre {n1} x {n2} = {n1 * n2}. ')
#
#     elif opcao == 3:
#         if n1 > n2:
#             print(f'O maior número e o {n1}. ')
#         elif n1 < n2:
#             print(f'O maior número é o {n2}. ')
#         else:
#             print('Os dois números são iguais. ')
#
#     elif opcao == 4:
#         print('Informe novos números: ')
#         n1 = int(input('Primeiro número: '))
#         n2 = int(input('Segundo número: '))
#
#     elif opcao == 5:
#         print('Saindo do pragrama...')
#
#     else:
#         print('Opção inválida. Tente novamente')
#
# print('Fim do programa! Volte sempre!')
#
# print('Fim!')

# print('Desafio 60')
#
# numero = int(input('Digite um número para saber seu fatorial: '))
#
# c = numero
# fatorial = 1
#
# while c > 0:
#     print(f'{c} ', end='')
#     if c > 1:
#         print(f' x ', end='')
#     fatorial *= c

#     else:
#         print(f' = ', end='')

#     # print(f' x ' if c > 1 else ' = ', end='') -> opção das linas anteriores de if e else
#
#     c -= 1
# print(f'{fatorial}')
#
# print('Fim!')

# print('Desafio 61')
#
# # an = enésimo termo
# # a1 = primeiro termo
# # n = número de termos
# # r= razão
# # print('an = a1 + (n – 1) * r')
#
# primeiro = int(input('Primeiro Termo: '))
# razao = int(input('Razão da PA: '))
#
# termo = primeiro
# contador = 1
#
# while contador <= 10:
#     print(f'{termo}', end=' -> ')
#     termo += razao
#     contador += 1
# print('Fim!')

# --------------------------        ou          -----------------------
# num = int(input("digite um valor para calculo de PA: "))
# razao = int(input("digite o valor da razao: "))
# decimo = num + (10 - 1) * razao
#
# c = num
#
# while (c < decimo + razao):
#     print(f"{c} ", end="-> ")
#     c = c + razao
#
# print("ACABOU")


# print('Desafio 62')

# print('Fórmuda da PA:')
# print('enérsimo termo = (primeiro termo + (número de termos - 1) * razão')
#
# primeiro_termo = int(input('Primeiro Termo: '))
# razao = int(input('Razão da PA: '))
#
# termo = primeiro_termo
# contador = 1
# total = 0
# mais = 10
#
# while mais != 0:
#     total = total + mais
#     while contador <= 10:
#         print(f'{termo}', end=' -> ')
#         termo += razao
#         contador += 1
#     print('Pausa')
#     mais = int(input('Quntos termos mais deseja mostrar? '))
# print(f'Foram mostrados {total} termos da PA.')
#
# print('Fim!')


# print('Desafio 63')

# print('Sequencia de FIBONACCI.')
#
# fibonacci = int(input('Informe um número inteirto: '))
# n1 = 0
# n2 = 1
# while fibonacci > n1:
#     print(f'{n1} -> {n2} -> ', end='')
#     n1 += n2
#     n2 += n1
# print('FIM')


# print('Desafio 64')

# numero = 0
# soma_dos_numeros = 0
# qde_de_numeros_digitados = 0
# print('Digite 999 para finalizar. ')

# while True:
#     numero = int(input('Digite um número: '))
#     if numero == 999:
#         break

#     soma_dos_numeros += numero
#     qde_de_numeros_digitados += 1

# print(f'Foram digitados {qde_de_numeros_digitados} números ')
# print(f'A soma entre eles é {soma_dos_numeros} ')

# print('Fim!')

# print('Desafio 65')
#
# numero = 0
# soma_dos_numeros = 0
# qde_de_numeros_digitados = 0
# maior = 0
# menor = 0
#
# while True:
#     numero = int(input('Digite um número: '))
#     soma_dos_numeros += numero
#     qde_de_numeros_digitados += 1
#     continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
#
#     if qde_de_numeros_digitados == 1:
#         maior = numero
#         menor = numero
#     else:
#         if numero > maior:
#             maior = numero
#
#         if numero < menor:
#             menor = numero
#
#         if continuar == 'S':
#             print('Digite o próximo número: ')
#
#         else:
#             break
#
# media = soma_dos_numeros / qde_de_numeros_digitados
#
# print(f'A média é {media:.2f} ')
# print(maior)
# print(menor)
#
# print('Fim!')


# print('Desafio 66')
# # repetido -> igual ao exercicio 64
#
# contador = 0
# soma = 0
#
# while True:
#     numero = int(input('Digite um número: '))
#
#     if numero != 999:
#         contador += 1
#         soma += numero
#
#     if numero == 999:
#         break
#
# print(f'Você digitou {contador} vezes.')
# print(f'A soma desses {soma} numeros é {soma}')


# Desafio 67
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando for negativo.

# numero = 0
#
# while True:
#     numero = int(input('Digite um número pra saber sua tabuada: '))
#     if numero < 0:
#         break
#     for contador in range(1, 11):
#         print(f'{numero} x {contador} = {numero * contador}')
#
# print('Cálculo das tabuadas "Encerrado"!')
#
# print('Fim!')



# Desafio 68
# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# from random import randint
#
# vitoria = 0
#
# while True:
#     jogador = int(input('Digite um número: '))
#     computador = randint(0, 10)
#     soma = jogador + computador
#     escolha = ' '
#
#     while escolha not in 'PI':
#         escolha = str(input('Qual você escolhe, Par ou Ímpar [P/I]? ')).strip().upper()[0]
#
#     if escolha == 'P':
#         if soma % 2 == 0:
#             vitoria += 1
#             print('Você Venceu!...Jogue novamente!')
#
#         else:
#             print('Você Perdeu!')
#             break
#
#     if escolha == 'I':
#         if soma % 2 == 1:
#             vitoria += 1
#             print('Você Venceu!...Jogue novamente!')
#
#         else:
#             print('Você Perdeu!')
#             break
#
# print(f'Você venceu {vitoria}')
# print('Fim!')


# from random import randint
#
# vitoria = 0
#
# while True:
#     escolha = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
#
#     while escolha not in 'PI':
#         print('Erro...escolha P ou I')
#         escolha = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
#
#     jogador = int(input('Digite um número: '))
#     computador = randint(0, 10)
#     print(f'O computador jogou {computador}')
#
#     soma = jogador + computador
#
#     if escolha == 'P':
#         if soma % 2 == 0:
#             vitoria += 1
#             print('Venceu. Jogue novamente..')
#
#         else:
#             print('Perdeu')
#             break

#     if escolha == 'I':
#         if soma % 2 == 1:
#             vitoria += 1
#             print('Venceu')
#
#         else:
#             print('Perdeu')
#             break
#
#
# print(f'Você venceu {vitoria} vezes.')

# =======================   ou   =======================

# from random import randint
# vitoria = 0
#
# while True:
#     jogador = int(input('Digite um número: '))
#     computador = randint(0, 10)
#
#     soma = jogador + computador
#     escolha = ' '
#
#     while escolha not in 'PI':
#         escolha = str(input('Par ou Ímpar? [P/I]')).strip().upper()
#
#         print(f'você jogou {jogador} e o computador jogou {computador} o total foi {soma}')
#
#         if escolha == 'P':
#             if soma % 2 == 0:
#                 print('Você Venceu')
#                 vitoria += 1
#
#         elif escolha == 'I':
#             print('Você Perdeu!')
#             break
#
#         if escolha == 'I':
#             if soma % 2 == 1:
#                 print('Você Venceu')
#                 vitoria += 1
#
#         elif escolha == 'I':
#             print('Você Perdeu!')
#             break
#         print('Jogue novamente...')
#
# print(f'Você venceu {vitoria} vezes.')
#
# print('Fim!')



'''Desafio 69
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A)	Quantas pessoas tem mais de 18 anos.
B)	Quantos homens foram cadastrados.
C)	Quantas mulheres tem menos de 20 anos.


maior_de_18 = homens_cadastrados = mulher_menos_de_20 = 0
while True:
    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    if idade >= 18:
        maior_de_18 += 1

    if sexo == 'M':
        homens_cadastrados += 1

    if sexo == 'F' and idade < 20:
        mulher_menos_de_20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print(f'Mais de 18 anos = {maior_de_18} pessoas ')
print(f'Homens cadastrados = {homens_cadastrados} ')
print(f'Mulheres com menos de 20 anos = {mulher_menos_de_20}')

print('Fim!') '''


''' Desafio 70
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total de gastos na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.


total_da_compra = 0
mais_de_1000 = 0
menor_preco = 0
cont_produtos = 0
mais_barato = ' '

while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço: R$ '))

    total_da_compra += preco
    cont_produtos += 1

    if preco > 1000:
        mais_de_1000 += 1

    if cont_produtos == 1:
        menor_preco = preco
        mais_barato = produto

    if preco < menor_preco:
        menor_preco = preco
        mais_barato = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N]')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'O produto mais barato é {mais_barato:.2f} e o preço é R$ {menor_preco} ')
print(f'{mais_de_1000} produtos custam mais de R$ 1.000,00 ')
print(f'Total da compra: R$ {total_da_compra:.2f}')
print('Fim!') '''


# total_da_compra = 0
# mais_de_1000 = 0
# menor_preco = 0
# contador = 0
# barato = ' '
#
# while True:
#     produto = str(input('Produto: '))
#     preco = float(input('Preço: R$ '))
#     total_da_compra += preco
#     contador += 1
#
#     if preco > 1000:
#         mais_de_1000 += 1
#
#     if contador == 1:
#         menor_preco = preco
#         barato = produto
#
#     else:
#         if preco < menor_preco:
#             menor_preco = preco
#             barato = produto
#
#     resposta = ' '
#     while resposta not in 'SN':
#         resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
#
#     if resposta == 'N':
#         break
#
# print(f'O valor taotal da compra é de R$ {total_da_compra:.2f} ')
# print(f'Temos {mais_de_1000} produtos custando mais de R$ 1000,00 ')
# print(f'O produto mais barato é R$ {barato}, que custa R$ {menor_preco:.2f}')
#
# print('Fim!')





# Desafio 71
# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada serão entregues.
# Obs: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10, R$ 1.

valor = int(input('Digite um valor para saque: R$ '))

while valor >= 50:
    if valor % 5 == 0:



print('você recebeu ')
print('Fim! ')







# Curso Python #17 – Listas (Parte 1)






# Desafio 78
# Faça um programa que leia 5 valores numéricos e guarde os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.







# Desafio 79
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados em uma ordem crescente.





# Desafio 80
# Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort( ) ).
# No final, mostre alista ordena na tela.






# Desafio 81
# Crie um programa que vá ler vários numéricos e colocar em uma lista.
# Depois disto mostre:
# a)	Quantos números foram digitados:
# b)	Alista de valores ordenada de forma crescente.
# c)	Se o valor 5 foi digitado e está ou não na lista.





# Desafio 82
# Crie um programa que vá ler vários números e colocar em uma lista.
# Depois disto, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.




# Desafio 83
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
