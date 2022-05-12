# Desafio 45
# Crie um programa que faça o computador jogar JOKENPÔ com você.


from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha uma opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qual é a jogada? '))
print('-=' * 12)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 12)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador Venceu!')
    elif jogador == 2:
        print('Computador Venceu!')
    else:
        print('Jogada inválida!')
elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('Computador Venceu!')
    elif jogador == 1:
        print('EMPATE!!')
    elif jogador == 2:
        print('Jogador Venceu')
    else:
        print('Jogada inválida!')
elif computador == 2: #CompuTador jogou TESOURA
    if jogador == 0:
        print('Jogador Venceu! ')
    elif jogador == 1:
        print('Computador Venceu!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')