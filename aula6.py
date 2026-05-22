# Conversão de tipos ( tambem chamado de coersão, typeconversion, typecasting, coercion)
# É o ato de converter um tpo em outro
# Tipos imútaveis e primitivos: str, int, float e bool
print("=====> SOMA DE TIPOS <=====")
print("Soma de tipos iguais: ", 1 + 1)
print("Soma de tipos iguais: ", 'a' + 'b')
# print("Soma de tipos diferentes: ", '1' + 1) #retorna TypeError

print("\n=====> CONVERSÃO <=====")
print(int('1'), type (int('1')))
print("O resultado de '1' + 1 é: ", (int('1') + 1))
print("O resultado de '1.5' + 2 é: ", (float('1.5') + 2))
print("O resultado de bool(' ') é: ", bool(' '))
print("O resultado de 11 + 'b' é: ", (str(11) + 'b'))