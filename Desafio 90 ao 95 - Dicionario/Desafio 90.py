# Exercício Python 090:
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno['nome'] = str(input('Nome: ')).strip().upper()
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado! '
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} = {v}')

#---------------  ou   ----------------------
print(f'{aluno["nome"]}: {aluno["situacao"]}')