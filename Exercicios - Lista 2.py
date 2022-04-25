# Exercício Python 084:
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.


dados_nome = []
dados_peso = []
cont_pessos = 0

while True:
    dados_nome.append(str(input('digite seu nome : ')))
    dados_peso.append(float(input('digite seu peso : ')))

    cont_pessos += 1

    resp = str(input('quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break

print('-' * 30)
# print(f'Foram cadastrados {len(dados_nome)} pessoas.') # usando o comando len()
print(f'Foram cadastrados {cont_pessos} pessoas.') # usando o comando max()

for nome, peso in enumerate(dados_peso):
    if peso == min(dados_peso):
        print(f'Com {peso} kg, a pessoa mais leve é {dados_nome[nome]}')
    if peso == max(dados_peso):
        print(f'Com {peso} kg, a pessoa mais pesada é {dados_nome[nome]}')











# lista_temporaria = []
# lista_principal = []
# pessoas_cadastradas = 0
# maior_peso = 0
# menor_peso = 0
#
# while True:
#     lista_temporaria.append(str(input('Nome: ')))
#     lista_temporaria.append(float(input('Peso: ')))
#     lista_principal.append(lista_temporaria[:])
#     lista_temporaria.clear()
#
#     pessoas_cadastradas += 1
#
#     if pessoas_cadastradas == 0:
#         maior_peso = menor_peso = lista_temporaria[1]
#     else:
#         if lista_temporaria[1] > maior_peso:
#
#
#
#
#     resposta = str(input('Deseja Continuar: [S/N] ')).strip().upper()[0]
#     if resposta in 'N':
#         break
#
# print('-' * 30)
# print(f'Você cadastrou {lista_principal} pessoas')
# print(f'Você cadastrou {pessoas_cadastradas} pessoas.') #usando contador
# # print(f'Você cadastrou {len(lista_principal)} pessoas.') #usando len()
# # print(f'A pessou mais pesada é {max(lista_temporaria[1])}')
# # print(f'A pessou mais leve é {min(lista_temporaria[1])}')




















# temp = []
# princ = []
#
# while True:
#     temp.append(str(input('Nome: ')))
#     princ.append(float(input('Peso: ')))
#     princ.append(temp[:])
#     temp.clear()
#     resp = str(input('Deseja Continuar? [S/N]'))
#     if resp in 'Nn':
#         break
#
# print('-' * 30)
# print(f'{temp} e {princ}')
# print('-' * 30)
#
# print(f'Ao todo você cadastrou {len(temp)} pessoas.')







# Exercício Python 085:
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.




# Exercício Python 086:
# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.



# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.



# Exercício Python 088:
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.



# Exercício Python 089:
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.


