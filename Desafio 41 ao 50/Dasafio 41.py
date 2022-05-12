# Desafio 41
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo coma idade:
# 	Até 9 anos: Mirim
# 	Até 14 anos: infantil
# 	Até 19 anos: Junior
# 	Até 25 anos: Sênior
# 	Acima: Master

from datetime import date
ano_atual = date.today().year
nascimento = int(input('Qual o ano de nascimento: '))
idade = ano_atual - nascimento
print(f'Quem nasceu em {nascimento} tem atualmente {idade} anos em {ano_atual}')
if idade <= 9:
    print('Sua categoria é Mirim.')
elif idade <= 14:
    print(' Sua categoria é Infantil.')
elif idade <=19:
    print('Sua categoria é Junior! ')
elif idade <=25:
    print('Sua categoria é Sênior!')
else:
    print('Sua categoria é Master! ')