# Exercício Python 089:
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
# de cada aluno individualmente.

boletim = []

while True:
    aluno = str(input('Nome: ')).strip().upper()
    nota_1 = float(input('1ª nota: '))
    nota_2 = float(input('2ª nota: '))
    media = (nota_1 + nota_2) / 2
    boletim.append([aluno, [nota_1, nota_2], media])

    resp = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

for posicao, nome_e_media in enumerate(boletim):
    print(f'{posicao} -> Nome: {nome_e_media[0]}, média {nome_e_media[2]}')



# boletim = []
#
# while True:
#     aluno = (str(input('Nome: ')))
#     nota_1 = (float(input('Nota 1: ')))
#     nota_2 = (float(input('Nota 2: ')))
#     media = (nota_1 + nota_2) /2
#     boletim.append([aluno, [nota_1, nota_2], media])
#
#     resp = str(input('Cadastrar mais: [S/N]')).strip().upper()[0]
#     if resp in 'N':
#         break
#
# print('-' * 30)
# print(f'{"Nº":<4} {"Nome":<10} {"Média":>8}') # formatação para nº, nome e média
# print('-' * 30)
# for posicao, nome_e_media in enumerate(boletim):
#     print(f'{posicao:<4} {nome_e_media[0]:<10} {nome_e_media[2]:>8}') # posição(0, 1, 2)
#                                                                       # nome_e_media[0] -> posição [0] na lista (nome)
#                                                                       # nome_e_media[2] -> posição [2] na lista (media)
#
# while True:
#     opcao = int(input('Mostrar as notas de qual aluno: (999 interrompe...)'))
#     if opcao == 999:
#         break
#     if opcao <= len(boletim) - 1:
#         print(f'Notas de {boletim[opcao][0]} são {boletim[opcao][1]}')# lotetim[opcao][0] -> posição [0] na lista (nome)
#                                                                       # boletim[opcap][1] -> posição [1] mostras as notas 1 e 2


# boletim = []
#
# while True:
#     aluno = str(input('Qual o nome do aluno? ')).strip().title()
#     note_1 = float(input('Qual a nota do aluno? '))
#     note_2 = float(input('Qual a segunda nota do aluno? '))
#     media = (note_1 + note_2) / 2
#
#     boletim.append([aluno, [note_1, note_2], media])
#
#     pergunta = str(input('Deseja resgistrar outro aluno? [S/N] ')).strip().upper()[0]
#     if pergunta not in 'SN':
#         print('\033[33mNão entendi...', end=' ')
#         pergunta = str(input('\033[mResponda com [S/N]: ')).strip().upper()[0]
#         if pergunta == 'N':
#             break
#     if pergunta == 'N':
#         break
#
# print('-=' * 5, 'BOLETIM', '=-' * 5)
# print(f'{"Nº":<4}{"NOME ":<10}{"NOTA":>8}')
# print('-' * 25)
#
# for nome, nota_media in enumerate(boletim):
#    print(f'{nome:<4}{nota_media[0]:<10}{nota_media[2]:>8}')
#
# while True:
#     continuar = int(input('Digite o número do aluno para ver a nota (999 para parar): '))
#     if continuar == 999:
#         break
#     if continuar <= len(boletim):
#         print(f'As notas do aluno {boletim[continuar][0]} são {boletim[continuar][1]}')
