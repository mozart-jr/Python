# Desafio 8
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetro e milímetros.

metro = int(input('informe a medida:'))
print(f'convertendo {metro}m para milímetros -> {metro * 1000}mm')
print(f'convertendo {metro}m para centímetros -> {metro * 100}cm')