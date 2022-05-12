# Desafio 29
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 Km/h mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.


print('VELOCIDADE MÁXIMA PERMITA NA RODOVIA: 80 Km/h')

velocidade = int(input('Informe a velocidae máxima do Veículo: '))
multa = (velocidade - 80) * 7

if velocidade <= 80:
    print('Dentro da velocidade máxima permita. Boa Viagem !!!')
else:
    print(f'ACIMA DA VELOCIDADE MÁXIMA PERMITA... Multa de R$ {multa:.2f}')