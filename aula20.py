# EXERCÍCIO EM PYTHON COM IF E COMPARAÇÃO 

print('==================================')
print('|SISTEMA DE COMPARAÇÃO DE VALORES|')
print('==================================')
primeiro_valor = input('\nDigite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'\nO primeiro valor ({primeiro_valor}) é maior que o segundo valor ({segundo_valor})')
elif segundo_valor > primeiro_valor:
    print(f'\nO segundo valor ({segundo_valor}) é maior que o primeiro valor ({primeiro_valor})')
else:
    print(f'\nOs valores são iguais: {primeiro_valor}')