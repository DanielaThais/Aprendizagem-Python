"""
INTERPOLAÇÃO BÁSICA DE STRINGS

s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789
"""

nome = "Daniela"
preco = 1000.95897643
variavel = '%s, o preço total foi de R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %02x' % (15, 15))