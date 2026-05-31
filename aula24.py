# OPERADORES LÓGICOS
# in e not in: strings são iteráveis
# 0 1 2 3 4 5 6 
# D a n i e l a
# 7 8 9 0 9 8 7

# nome = 'Daniela'

# print (nome[2])
# print (nome[-4])

# print('ela' in nome)
# print('zero' in nome)
# print( 10 * '=')
# print('Dani' not in nome)
# print('zero' not in nome)

print('======> SISTEMA DE NOMES <=====')
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')