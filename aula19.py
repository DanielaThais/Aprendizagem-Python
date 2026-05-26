""" OPERADORES DE COMPARAÇÃO (RELACIONAIS)

|OP      |SIGNIFICADO         |EXEMPLO (True)
|>       |maior               |2 > 1
|>=      |maior ou igual      |2 >= 2
|<       |menor               |1 < 2
|<=      |menor ou igual      |2 <= 2
|==      |igual               |'a' == 'a'
|!=      |diferente           |'a' != 'b'    
"""

maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'

print('**** RESULTADOS DAS COMPARAÇÕES ****')
print('\n2 > 1? =>', maior)
print('2 >= 2? =>', maior_ou_igual)
print('1 < 2? =>', menor)
print('2 <= 2? =>', menor_ou_igual)
print("'a' == 'a'? =>", igual)
print("'a' != 'b'? =>", diferente)