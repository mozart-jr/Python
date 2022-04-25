# Desafio: Área do Círculo
# A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:
# - Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.
#
# Entrada
# A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.
#
# Saída
# Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal.
# Utilize variáveis de dupla precisão (double).
# Como todos os problemas, não esqueça de imprimir o fim de linha após o resultado,
# caso contrário, você receberá "Presentation Error".

# raio = float(input())
# pi = 3.14159
# area = pi * (raio ** 2)
# print(f'A={area:.4f}')

# Desafio: SOMA SIMPLES
# Leia dois valores inteiros, no caso para variáveis A e B.
# A seguir, calcule a soma entre elas e atribua à variável SOMA.
# A seguir escrever o valor desta variável.
#
# Entrada
# O arquivo de entrada contém 2 valores inteiros.
#
# Saída
# Imprima a mensagem "SOMA" com todas as letras maiúsculas, com um espaço em branco antes e depois da igualdade
# seguido pelo valor correspondente à soma de A e B. Como todos os problemas, não esqueça de imprimir o fim de linha
# após o resultado, caso contrário, você receberá "Presentation Error".

# a = int(input())
# b = int(input())
# print(f'SOMA = {a + b}')

# Desafio: PRODUTO SIMPLES
# Leia dois valores inteiros.
# A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD.
# A seguir mostre a variável PROD com mensagem correspondente.
#
# Entrada
# O arquivo de entrada contém 2 valores inteiros.
#
# Saída
# Imprima a mensagem "PROD" e a variável PROD conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.
# Não esqueça de imprimir o fim de linha após o produto, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

# a = int(input())
# b = int(input())
# print(f'PROD = {a * b}')

# Desafio: MÉDIA 1
# Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno.
# A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11).
# Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
#
# Entrada
# O arquivo de entrada contém 2 valores com uma casa decimal cada um.
#
# Saída
# Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 5 dígitos após o ponto decimal
# e com um espaço em branco antes e depois da igualdade. Utilize variáveis de dupla precisão (double) e como todos os problemas,
# não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".


# Cálculo da média ponderada
# Mp = [(N1 x P1) + (N2 x P2) + (N3 x P3) + ... (Nx x Px)] ÷ (P1 + P2 + P3 + ... Px).
# Mp é a média ponderada (o resultado que você quer descobrir)
# N é cada valor do conjunto
# P é o peso correspondente de cada valor do conjunto.

# a = float(input()) * 3.5
# b = float(input()) * 7.5
# media = (a + b) / (3.5 + 7.5)
# print(f'MEDIA = {media:.5f}')


# Desafio: MÉDIA 2
# Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno,
# sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5.
# Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
#
# Entrada
# O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).
#
# Saída
# Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 1 dígito após o ponto decimal
#  com um espaço em branco antes e depois da igualdade. Assim como todos os problemas, não esqueça de imprimir
# o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

# a = float(input()) * 2
# b = float(input()) * 3
# c = float(input()) * 5
# media = (a + b + c) / (2 + 3 + 5)
# print(f'MEDIA = {media:.1f}')

# Desafio: DIFERENÇA
# Leia quatro valores inteiros A, B, C e D.
# A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula:
# DIFERENCA = (A * B - C * D).
#
# Entrada
# O arquivo de entrada contém 4 valores inteiros.
#
# Saída
# Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco
# antes e depois da igualdade.

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# diferenca = (a * b) - (c * d)
# print(f'DIFERENCA = {diferenca}')


# Desafio: SALÁRIO
# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora
# e calcula o salário desse funcionário.
# A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
#
# Entrada
# O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de
# horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.
#
# Saída
# Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da igualdade.
# No caso do salário, também deve haver um espaço em branco após o $.

# numero = int(input())
# horas_trabalhadas = int(input())
# valor_por_hora = float(input())
# salary = horas_trabalhadas * valor_por_hora
# print(f'NUMBER = {numero}')
# print(f'SALARY = U$ {salary:.2f}')


# Desafio: SALÁRIO COM BONUS
# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).
# Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês,
# com duas casas decimais.
#
# Entrada
# O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais,
# representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente.
#
# Saída
# Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

# nome = str(input())
# salario_fixo = float(input())
# total_vendas = float(input())
# comissao = salario_fixo + (total_vendas *0.15)
# print(f'TOTAL = R$ {comissao:.2f}')


# Desafio: CALCULO SIMPLES
# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1,
# o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
#
# Entrada
# O arquivo de entrada contém duas linhas de dados.
# Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.
#
# Saída
# A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos
# e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

# cod_1, qtde_1, valor1 = input().split(' ')
# cod_1 = int(cod_1)
# qtde_1 = int(qtde_1)
# valor1 = float(valor1)
# cod_2, qtde_2, valor2 = input().split(' ')
# cod_2 = int(cod_2)
# qtde_2 = int(qtde_2)
# valor2 = float(valor2)
#
# # cod_1, qtde_1, valor1 = int(input()), int(input()), float(input())
# # cod_2, qtde_2, valor2 = int(input()), int(input()), float(input())
# total = (qtde_1 * valor1) + (qtde_2 * valor2)
# print(f'VALOR A PAGAR: R$ {total:.2f}')


# Desafio: ESFERA
# Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R).
# A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o valor 3.14159.
#
# Dica: Ao utilizar a fórmula, procure usar (4/3.0) ou (4.0/3), pois algumas linguagens (dentre elas o C++), assumem
# que o resultado da divisão entre dois inteiros é outro inteiro.
#
# Entrada
# O arquivo de entrada contém um valor de ponto flutuante (dupla precisão), correspondente ao raio da esfera.
#
# Saída
# A saída deverá ser uma mensagem "VOLUME" conforme o exemplo fornecido abaixo, com um espaço antes e um espaço
# depois da igualdade. O valor deverá ser apresentado com 3 casas após o ponto.

# raio = int(input())
# pi = 3.14159
# volume = (4/3.0) * pi *(raio ** 3)
# print(f'VOLUME = {volume:.3f}')

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

# a, b, c = input().split(' ')
# a = float(a)
# b = float(b)
# c = float(c)
#
# pi = 3.14159
#
# triangulo = (a * c) / 2
# circulo = pi * (c ** 2)
# trapezio = ((a + b) * c) / 2
# quadrado = b * b
# retangulo = a * b

# print(f'TRIANGULO: {triangulo:.3f}')
# print(f'CIRCULO: {circulo:.3f}')
# print(f'TRAPEZIO: {trapezio:.3f}')
# print(f'QUADRADO: {quadrado:.3f}')
# print(f'RETANGULO: {retangulo:.3f}')