# EXERCÍCIOS DE FIXAÇÃO

"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

print('==========> Bem vindo ao Exercício 3 <==========')
primeiro_nome = input('\nDigite o seu primeiro nome: ')

primeiro_nome_tamanho = len(primeiro_nome)

if primeiro_nome_tamanho <= 4:
    print('Seu nome é curto')
elif primeiro_nome_tamanho >= 5 and primeiro_nome_tamanho <= 6:
    print('Seu nome é normal')
else:   
    print('Seu nome é muito grande')