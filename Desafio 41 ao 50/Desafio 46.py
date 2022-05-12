# Desafio 46
# Faça um programa que mostre na tela de contagem regressiva para o estouro de fogos de artifício indo de 10 até 0, com uma pauso de 1 segundo entre elas.


from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('Feliz ano novo!!')



