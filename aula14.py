# Formatação de strings com o método format

a = 'A'
b = 'B'
c = 1.1
formato = 'a = {} \nb = {} \nc = {numerico:.2f}'.format(a, b, numerico=c) #sempre que um argumento recebe uma noemação ele passa a ser um parâmetro e sues sucessores SEMPRE deverão seguir o mesmo padrão

print(formato)