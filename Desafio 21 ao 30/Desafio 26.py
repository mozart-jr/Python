# Desafio 26
# Faça um programa que leia uma frase pelo teclado e mostre:
# 	quantas vezes apareceu a letra “A”;
# 	em que posição ela apareceu pela primeira vez;
# 	em que posição ela apareceu pela última vez.

frase = str(input('Digite uma frase: ')).strip().upper()
letra = str(input('Qual letra deseja contar: ')).strip().upper()

if letra in frase:
    print(f'A letra "{letra}" foi digitada {frase.count(letra)} vezes')
else:
    print(f'A letra "A" não foi digitada...')

print(f'A letra "{letra}" apareceu pela Primeira vez na posição {frase.find(letra) + 1} ')
print(f'A letra "{letra}" apareceu pela Ultima vez na posição {frase.rfind(letra) + 1} ')
