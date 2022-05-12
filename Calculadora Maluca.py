print('-' * 30)
print('CALCULADORA MALUCA')
print('-' * 30)

a = float(input('digite um número: '))
b = float(input('digite outro número: '))

soma = a + b
sub = a - b
mult = a * b
div = a / b

operacao = input('''
Selecione a opção desejada: 
[1] -  Soma
[2] Subtraçao
[3] Multiplicação
[4] Divisão
[5] Potenciação
[6] Círculo
[7] Quadrado
[8] Trapézio
[9] Retângulo
''')

if operacao == '1':
    print(f'{a} + {b} = {soma}')

elif operacao == '2':
    print(f'{a} - {b} = {sub}')

elif operacao == '3':
    print(f'{a} * {b} = {mult}')

elif operacao == '4':
    print(f'{a} / {b} = {div}')

else:
    print('Você digitou uma opção inválida, por favor retorne ao programa novamente...')
