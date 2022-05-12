# Desafio 25
# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Tem "SILVA" no nome? ')).strip().upper()

if 'SILVA' in nome.split():
    print(f'{nome} -> Tem "SILVA" no nome!!')
else:
    print(f'{nome} -> "NÃO" tem "SILVA" no nome!!')
