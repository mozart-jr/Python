# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# for comida in lanche:
#     print(f'Eu vou comer {comida}!')

#USANDO -> len()

# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]}')

########### ----- ############

# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# # len() -> conta quantos itens tem. Exemplo acima = 4
# print(len(lanche))
# print('Eu comi pra caramba...')

########### ----- ############

# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# for posicao, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {posicao}.')

#USANDO -> len()

# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}.')



# RESUMINDO - AS MELHORS CONDIÇÕES
#
# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#
# for comida in lanche:
#     print(f'Eu vou comer {comida}!')
#
# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]}')
#
# for posicao, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {posicao}.')
#
# #mostra na tela em ordem crescente
# print(sorted(lanche))

# valores = []
# valores.append(9)
# valores.append(5)
# valores.append(3)
#
# for pos, val in enumerate(valores):
#     print(f'Na posição {pos} encontrei o valor {val}...')


# valores = []
# for c in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
#
# for pos, val in enumerate(valores):
#     print(f'Na posição {pos} encontrei o valor {val}...')