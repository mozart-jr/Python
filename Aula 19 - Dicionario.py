# # dados = dict()  ou dados = {}
#
#
# dados = {'nome':'Pedro', 'idade': 25}
# print(dados['nome'])    # ->Pedro
# print(dados['idade'])   # -> 25
#
# # Adicionar elemento
# dados['sexo'] = 'M'   # -> Vai criar o elemento 'sexo' e vai coloca o 'M' dentro dele
#
# # Remover elementos
# del dados['idade']    # -> remove o dados 'idade', isto é, deleta 'idade' e deleta 25
#
# -------------------------------------------------------------------------------------------------------------
#
# filme = {'titulo':'Star Wars',
#          'ano':1977,
#          'diretor':'George Lucas'
#         }
# print(filme.values())  # .values() -> retorna todos os valores do dicionário: 'Star Wars' 1977 'George Lucas'
# print(filme.keys())    # .keys() -> retorna todos as chaves do dicionário: 'nome' 'idade' 'sexo'
# print(filme.items())   # .items() -> retorna todos as chaves e todos os valores do dicionário:
# #                        # 'Star Wars' 1977 'George Lucas'
#                        # 'nome' 'idade' 'sexo'
#
# # -> usando com for...
# for k, v in filme.items():
#     print(f'O {k} é {v}')   # -> k = título, ano, diretor
# #                             # -> v = Star Wars, 1977, George |LUcas
#
#                             # resposta: # O titulo é Star Wars
#                                         # O ano é 1977
#                                         # O diretor é George Lucas
#
# ---------------------------------------------------------------------------------------------------------------------
#
# # Cópia no dicionário
#
# locadora = [{'titulo':'Star Wars', 'ano':1977, 'diretor':'George Lucas'},
#            {'titulo':'Avengers', 'ano':2012, 'diretor':'JossWhedon'},
#            {'titulo':'Matrix', 'ano':1999, 'diretor':'Wachowski'}]
#
# print(locadora[0]['ano'])       # -> 1977
# print(locadora[2]['titulo'])    # -> Matrix

# ---------------------------------------------------------------------------------------------------------------------
#EXERCÍCIOS DE AULA

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(pessoas)      # {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(pessoas['nome'])      # Gustavo
# print(pessoas['idade'])     # 22
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos. ') # O Gustavo tem 22 anos.
# print(pessoas.keys())    # dict_keys(['nome', 'sexo', 'idade'])
# print(pessoas.values())  # dict_values(['Gustavo', 'M', 22])
# print(pessoas.items())   # dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])
# ------------------   RESPOSTA   ------------------------
# {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# Gustavo
# 22
# O Gustavo tem 22 anos.
# dict_keys(['nome', 'sexo', 'idade'])
# dict_values(['Gustavo', 'M', 22])
# dict_items([('nome', 'Gustavo'), ('sexo', 'M'), ('idade', 22)])

# ---------------------------------------------------------------------------------------------------------------------

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# for k in pessoas.keys():
#     print(k)

# Respota:
# nome
# sexo
# idade

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# for k in pessoas.values():
#     print(k)

# Respota:
# Gustavo
# M
# 22

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
#
# # Respota:
# nome = Gustavo
# sexo = M
# idade = 22

# ---------------------------------------------------------------------------------------------------------------------
# Usasando o comando del

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# del pessoas['sexo']
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# # Respota:
# nome = Gustavo
# idade = 22

# ---------------------------------------------------------------------------------------------------------------------
# Mudando o nome de Gustavo para Leandro

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# pessoas['nome'] = 'Leandro'
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# Respota:
# nome = Leandro
# sexo = M
# idade = 22

# ---------------------------------------------------------------------------------------------------------------------

# Adicionando

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# pessoas['peso'] = 98.5
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# Respota:
# nome = Gustavo
# sexo = M
# idade = 22
# peso = 98.5

# ---------------------------------------------------------------------------------------------------------------------

# Criando Dicionário dentro de uma Lista

# brasil = []
# estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
# estado2 = {'SP':'São Paulo', 'sigla':'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(estado1)
# print(estado1)

# Respota:
# {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
# {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}

# ---------------------------------------------------------------------------------------------------------------------

# brasil = []
# estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
# estado2 = {'SP':'São Paulo', 'sigla':'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil)

# Respota:
# [{'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}, {'SP': 'São Paulo', 'Sigla': 'SP'}]

# ---------------------------------------------------------------------------------------------------------------------

# brasil = []
# estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
# estado2 = {'SP':'São Paulo', 'sigla':'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0])

# Respota:
# {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}

# ---------------------------------------------------------------------------------------------------------------------

# brasil = []
# estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
# estado2 = {'SP':'São Paulo', 'sigla':'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0]['uf'])
# print(brasil[1]['sigla'])
#
# # Respota:
# Rio de Janeiro
# SP

# ---------------------------------------------------------------------------------------------------------------------
# Utilizando o comando -> COPY()

# estado = {}     # pode ser escrito -> estado = dict() -> PARA DICIONÁRIO {}
# brasil = []     # pode ser escrito -> brasil = list() -> PARA LISTA []
# for c in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Sigla: '))
#     brasil.append(estado.copy())
# print(brasil)

# Respota:
# [{'uf': 'minas', 'sigla': 'mg'}, {'uf': 'sampa', 'sigla': 'sp'}, {'uf': 'acre', 'sigla': 'ac'}]

# ---------------------------------------------------------------------------------------------------------------------

# estado = {}     # pode ser escrito -> estado = dict() -> PARA DICIONÁRIO {}
# brasil = []     # pode ser escrito -> brasil = list() -> PARA LISTA []
# for c in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Sigla: '))
#     brasil.append(estado.copy())
# for state in brasil:
#     print(state)

# Respota:
# {'uf': 'minas', 'sigla': 'mg'}
# {'uf': 'sampa', 'sigla': 'sp'}
# {'uf': 'acre', 'sigla': 'ac'}

# ---------------------------------------------------------------------------------------------------------------------

# estado = {}     # pode ser escrito -> estado = dict() -> PARA DICIONÁRIO {}
# brasil = []     # pode ser escrito -> brasil = list() -> PARA LISTA []
# for c in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Sigla: '))
#     brasil.append(estado.copy())
# for state in brasil:
#     for v in state.values():
#         print(v, end=' ')
#     print()     # esse printa é para poder pular uma lina, já que o exercicio acaba na linha anterior..precisa desse print()

# Respota:
# minas mg
# sampa sp
# bahia ba