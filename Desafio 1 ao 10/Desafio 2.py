# Desafio 2
# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

nome = str(input('Qual é o seu nome: ')).upper()
dia = int(input('Qual é o dia do seu nascimento: '))
mes = int(input('qual é o mês do seu nascimento: '))
ano = int(input('Qual é o ano do seu nascimento: '))
print(f'Olá, {nome}, você nasceu no dia {dia}/{mes}/{ano}')
