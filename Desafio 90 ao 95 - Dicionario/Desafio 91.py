# Exercício Python 091:
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter
from time import sleep

jogos = {}
print('Valores sorteados:')
for j in range(1, 5):
    jogos[f'jogador{j}'] = randint(1, 6)

for k, v in jogos.items():
    sleep(1)
    print(f'O {k} tirou {v}')

podio = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print('Ranking dos Jogadores:')
print('O maior valor vence!')

for i, v in enumerate(podio):
    sleep(1)
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')

# from random import randint
# from time import sleep
# from operator import itemgetter
#
# ranking = {}
# jogo = {'jogador 1': randint(1, 6),
#         'jogador 2': randint(1, 6),
#         'jogador 3': randint(1, 6),
#         'jogador 4': randint(1, 6)}
#
# print('Números Sorteados: ')
# for k, v in jogo.items():
#     print(f'{k} tirou "{v}" no dado.')
#     sleep(0.5)
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print(ranking)
