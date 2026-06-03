"""
EXERCÍCIO

Peça ao usuário para digitar o nome e a idade. 

Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém ou não espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}

Se nada for digitado em nome ou idade:
    Exiba:
        Desculpe, você deixou campos vazios.
"""

print('======> SEJA BEM-VINDO(A) <=====')
nome = input('\nDigite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade != '':
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome contém espaços: {" " in nome}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('\nErro: Desculpe, você deixou campos vazios.')   

print('\nAté breve!')
print("================================")