# Desafio 28
# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5)

jogador = int(input('Escolha um número entre 0 e 5: '))

if jogador == computador:
    print('Você acertou!')

else:
    print('Você errou...')

sleep(0.5)
print(f'O computador jogou {computador} e você jogou {jogador}')
print('Fim...')
