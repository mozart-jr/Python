# Desafio 13
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário: R$ '))
aumento = 1.15
novo_salario = salario * aumento
print(f'O valor do novo salário é de R$ {novo_salario:.2f}')
print('FIM!')
