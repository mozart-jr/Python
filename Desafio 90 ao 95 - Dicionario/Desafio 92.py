# Exercício Python 092:
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

dados = {}
dados['nome'] = str(input('Nome: '))

ano_nasc = int(input('Ano de Nascimento: '))
# data_atual = date.today()
ano_atual = date.today().year
# ano_atual = data_atual.year

dados['idade'] = ano_atual - ano_nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = int(input('Salário: R$ '))
    dados['aposentadoria'] = (dados['contratação'] - ano_nasc) + 35

print('-'*59)
for k, v in dados.items():
    print(f'- {k}: {v}')


# from datetime import datetime
#
# cadastro = {}
# cadastro['nome'] = str(input('Nome: '))
# nasc = int(input('Ano de Nascimento: '))
# cadastro['idade'] = datetime.now().year - nasc
# cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
# if cadastro['ctps'] != 0:
#     cadastro['contratacao'] = int(input('Ano de Contratação: '))
#     cadastro['salario'] = float(input('Salário R$: '))
#     cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratacao'] + 35) - datetime.now().year)
#
# print('-' * 30)
# for k, v in cadastro.items():
#     print(f' -> {k}: {v}')

