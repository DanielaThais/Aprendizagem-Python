"""
FORMATAÇÃO BÁSICA DE STRING

s = string
d = int
f = float
. = <número de dígitos>f
x ou X = hexadecimal
> = esquerda
< = direita
^ = centro
+ ou - = sinal

Exemplo: 0>-100,.1f
Conversion flags - !r !s !a

"""
variavel = 'Dani'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{variavel:i<10}')
print(f'O hexadecimal de 1500 é {1500:08X}')