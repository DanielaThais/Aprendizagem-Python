"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321

Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade de carracteres da string
"""

variavel = 'Olá mundo'
print(variavel[-4])     #pega somente o 'u'
print(variavel[4:])     #pega o 'mundo'
print(variavel[0:4])    #pega o 'Olá'
print(len(variavel))    #retorna a quantidade de caracteres da string
print(variavel[0:9:2])  #passar determinada quantidade de caracteres
print(variavel[-1:-10:-1])  #passar determinada quantidade de caracteres espelhado