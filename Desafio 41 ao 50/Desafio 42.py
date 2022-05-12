# Desafio 42
# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# 	Equilátero: Todos os lados iguais
# 	Isósceles: Dois lados iguais
# 	Escaleno: Todos os lados diferentes

r1 = float(input('Seguimento 1: '))
r2 = float(input('Seguimento 2: '))
r3 = float(input('Seguimento 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com estes seguimentos é possível formar um triângulo!')
    if r1 == r2 == r3:
        print('Triângulo Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Triângulo Escaleno!')
    else:
        print('Triângulo Isósceles!')
else:
    print('Este seguimento não formará um triângulo!')