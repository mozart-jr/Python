# Desafio 43
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# 	Abaixo dos 18.5:  Abaixo do peso
# 	Ente 18.5 e 25:  Peso ideal
# 	Entre 25 até 30:  Sobrepeso
# 	Entre 30 até 40:   Obesidade
# 	Acima de 40:  Obesidade mórbida

altura = float(input('Qual é a altura: '))
peso = float(input('Qual é o peso: '))
IMC = peso / (altura)**2
print(f'IMC de {IMC:.1f} ')
if IMC < 18.5:
    print('Abaixo do Peso. ')
elif IMC > 18.5 and IMC < 25:
    print('Peso Ideal. ')
elif IMC > 25 and IMC < 30:
    print('Sobrepeso. ')
elif IMC > 30 and IMC < 40:
    print('Obesidade. ')
else:
    print('Obesidade Mórbida. ')
