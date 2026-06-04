# EXERCÍCIOS DE FIXAÇÃO

"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print('==========> Bem vindo ao Exercício 2 <==========')
hora = input('\nDigite a hora atual em número inteiro: ')

hora = int(hora)

if hora >= 0 and hora <= 11:
    print('Bom dia!')
elif hora >= 12 and hora <= 17:
    print('Boa tarde!')
elif hora > 24:
    print('Hora inválida! Por gentileza execute novamente.')
else:
    print('Boa noite!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""