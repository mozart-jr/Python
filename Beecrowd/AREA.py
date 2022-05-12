# Desafio: ÁREA
# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.(A = (a * h) / 2
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.
#
# Entrada
# O arquivo de entrada contém três valores com um dígito após o ponto decimal.
#
# Saída
# O arquivo de saída deverá conter 5 linhas de dados.
# Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre
# os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.

a, b, c = input().split(' ')
a = float(a)
b = float(b)
c = float(c)

pi = 3.14159

triangulo = (a * c) / 2
circulo = pi * (c ** 2)
trapezio = ((a + b) * c) / 2
quadrado = b * b
retangulo = a * b

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')