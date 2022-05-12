# Exercício Python 088:
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.


from random import randint

palpite = [0, 0, 0, 0, 0, 0]

quantos_jogos = (int(input('Quantos jogos: ')))

for c in range(0, quantos_jogos):
    for jogos in range(0, 6):
        palpite[jogos] = randint(1, 60)
    print(f'Números sorteados: {sorted(palpite)}')


# from random import randint
# from time import sleep
#
# palpite = [0, 0, 0, 0, 0, 0]
# quantos = int(input('Quantos jogos você quer gerar? '))
#
# for jogos in range(0, quantos):
#     for num in range(0, 6):
#         palpite[num] = randint(1, 60)
#         sleep(0.1)
#
#     print(f'Os jogos foram: {sorted(palpite)}')
    # palpite.sort()
    # print(palpite)


# from random import randint
# jogos = []
# numero = []
#
# total_de_jogos = int(input("Quantos jogos deseja fazer? "))
#
# for c in range(0, total_de_jogos):
#     for j in range(0, 6):
#         n = randint(1, 60)
#         if n not in numero:
#             numero.append(n)
#         else:
#             n = randint(1, 60)
#             numero.append(n)
#     jogos.append(sorted(numero[:]))
#     numero.clear()
#
# for c, e in enumerate(jogos):
#     print(f'{c + 1}º Jogo = {e}')
