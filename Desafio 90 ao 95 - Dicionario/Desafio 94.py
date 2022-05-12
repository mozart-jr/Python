# Exercício Python 094:
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

dados = {}
pessoas = []

soma_idade = 0
media = 0

while True:
    dados.clear()
    dados['nome'] = str(input('Nome: ')).strip().upper()

    dados['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('OPÇÃO INVÁLIDA! .... Digite somente M ou F: ')).strip().upper()[0]

    dados['idade'] = int(input('Idade: '))
    soma_idade += dados['idade']

    continuar = str(input('Continuar? [S/N]')).strip().upper()[0]
    pessoas.append(dados.copy())
    if continuar == 'N':
        break



print('-' * 30)
print(pessoas)
media = soma_idade / len(pessoas)
print(f'A média de idade das possoas cadastradas é {media:.2f} anos. ')
print('-' * 30)






































#
# dados = {}
# pessoas = []
# soma_das_idades = 0
# media = 0
#
# while True:
# # "dados.clear()" -> Depois de adicionar um cadastro, limpa os dados para o proximo cadastro.
#     dados.clear()
#     dados['nome'] = str(input('Nome: ')).strip().upper()
#     dados['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
#     while dados['sexo'] not in 'MF':
#         dados['sexo'] = str(input('Erro....Por Favor, escolha somente M ou F...Sexo: ')).strip().upper()[0]
#     dados['idade'] = int(input('Idade: '))
#     soma_das_idades += dados['idade']
#
#     continuar = str(input('Deseja contiunar os Cadastros: [S/N]')).strip().upper()[0]
# # "pessoas.append(dados.copy())" -> Adiciona os dados de uma pessoa em uma lista e ja limpa para o próximo cadastro.
#     pessoas.append(dados.copy())
#     while continuar not in 'SN':
#         continuar = str(input('Erro...Por Favor, escolha somente S ou N ')).strip().upper()[0]
#     if continuar == 'N':
#         break
#
# print(f'A soma das idades é {soma_das_idades} anos. ')
# print(f'Foram cadastradas {len(pessoas)} pessoas. ')
#
# media = soma_das_idades / len(pessoas)
# print(f'A média das idades é de {media:.2f}')
#
# print('=-' * 30)
# print('As mulheres cadastradas foram:')
# for p in pessoas:
#     if p['sexo'] in 'Ff':
#         print(f'{p["nome"]}')
# print('=-' * 30)
#
# print('-' * 30)
# print('Pessoas com a idade acima da média: ')
# for p in pessoas:
#     if p['idade'] > media:
#         print(f'{p["nome"]}')
# print('-' * 30)
#
# print('FIM!!!! ')

# dados = {}
# pessoas = []
# soma = 0
# media = 0

# while True:
#     dados.clear()
#     dados['nome'] = str(input('Nome: ')).strip().upper()
#     dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
#     while dados['sexo'] not in 'MF':
#         dados['sexo'] = str(input('Por favor, digite apenas M ou F. '))

#     dados['idade'] = int(input('Idade: '))
#     soma += dados['idade']

#     continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
#     pessoas.append(dados.copy())
#     while continuar not in 'SN':
#         continuar = str(input('Por favor, digite apenas S ou N. ')).strip().upper()[0]
#     if continuar in 'N':
#         break

# print('-' * 72)
# print(f'Ao todo temos {len(pessoas)} pessoas cadastradas')
# media = soma / len(pessoas)
# print(f'A média de idade é de {media} anos')

# print('As mulheres cadastradas foram', end=' ')
# for p in pessoas:
#     if p['sexo'] in 'Ff':
#         print(f'{p["nome"]}', end=' ')
# print()
# print('Lista de pessoas que estão com a idade acima da média:', end=' ')
# for p in pessoas:
#     if p['idade'] > media:
#         print(f'{p["nome"]}', end=' ')
#     else:
#         print('Todos estão dentro da media', end=' ')
# print()
# print('\n<= ENCERRANDO =>')