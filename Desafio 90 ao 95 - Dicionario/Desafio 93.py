# Exercício Python 093:
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# jogador = {}
# partidas = []
# jogador['nome'] = str(input('Nome do jogador: ')).strip().upper()
# total_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
#
# for c in range(0, total_partidas):
#     partidas.append(int(input(f'Quants gols no {c + 1}º jogo? ')))
# jogador['gols'] = partidas[:]
# jogador['total '] = sum(partidas)
#
# print('-' * 30)
# print(jogador)
# print('-' * 30)
#
# for k, v in jogador.items():
#     print(f'O campo {k} tem o valor {v}')
# print('-' * 30)
# print(f'O jogoador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
# for i, v in enumerate(jogador['gols']):
#     print(f' -> na partida {i + 1} fez {v} gols. ')
# print(f'Foi um total de {jogador["total"]} gols. ')


jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {p + 1}? ')))
    jogador['gols'] = gols
    totalgols = sum(gols)
    jogador['total'] = totalgols

print('=-=' * 25)
print(jogador)
print('=-=' * 25)

for k, v in jogador.items():
    print(f'{k}: {v}')
print('=-=' * 25)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for p, g in enumerate(gols):
    print(f'  => Na partida {p + 1}, fez {g} gols.')
print(f'Foi um total de {sum(gols)} gols.')