# Exercício Python 084:
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista_nome = []
lista_peso = []
cont_pessoas = 0

while True:
    lista_nome.append(str(input('Nome: ')))
    lista_peso.append(float(input('Peso: ')))
    cont_pessoas += 1

    resp = str(input('DESEJA CONTINUAR? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break

for nome, peso in enumerate(lista_peso):
    if peso == min(lista_peso):
        print(f'MENOR PESO {lista_nome[nome]} ')
    if peso == max(lista_peso):
        print(f'MAIOR PESO {lista_nome[nome]} ')

print(f'Foram cadastradas {cont_pessoas} pessoas. ')


# lista_nome = []
# lista_peso = []
# cont_pessoas = 0
#
# while True:
#     lista_nome.append(str(input('digite seu nome : ')))
#     lista_peso.append(float(input('digite seu peso : ')))
#
#     cont_pessoas += 1
#
#     resp = str(input('quer continuar? [S/N] ')).strip().upper()[0]
#     if resp in 'N':
#         break
#
# print('-' * 30)
# # print(f'Foram cadastrados {len(dados_nome)} pessoas.') # usando o comando len()
# print(f'Foram cadastrados {cont_pessoas} pessoas.') # usando o comando max()
#
# for nome, peso in enumerate(lista_peso):
#     if peso == min(lista_peso):
#         print(f'Com {peso} kg, a pessoa mais leve é {lista_nome[nome]}')
#     if peso == max(lista_peso):
#         print(f'Com {peso} kg, a pessoa mais pesada é {lista_nome[nome]}')

#
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
# #     resposta = str(input('Deseja Continuar: [S/N] ')).strip().upper()[0]
#     if resposta in 'N':
#         break
#
# print('-' * 30)
# print(f'Você cadastrou {lista_principal} pessoas')
# print(f'Você cadastrou {pessoas_cadastradas} pessoas.') #usando contador
# print(f'Você cadastrou {len(lista_principal)} pessoas.') #usando len()
# print(f'A pessou mais pesada é {max(lista_temporaria[1])}')
# print(f'A pessou mais leve é {min(lista_temporaria[1])}')
