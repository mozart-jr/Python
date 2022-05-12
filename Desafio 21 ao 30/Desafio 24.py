# Desafio 24
# Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome “SANTO”

cidade = str(input('Esta cidade tem a palavra "SANTO" no nome? ')).strip().upper()

# if cidade[0].upper() == 'SANTO':
#     print('Esta cidade tem a palavra "SANTO" no nome')
# else:
#     print('Esta cidade "NÃO" tem a palavra "SANTO" no nome')
# print('FIM!!')

# ***************************************** ou *********************************************

if 'SANTO' in cidade[0].split():
    print('Esta cidade tem a palavra "SANTO" no nome')
else:
    print('Esta cidade "NÃO" tem a palavra "SANTO" no nome')
print('FIM!!')
