#ARITMÉTICOS

a = 2
b = 3

soma = a + b
print(soma)

sub = a - b
print(sub)

multi = a * b
print(multi)

div = a / b
print(div)
#Divisão normal considerando o ponto flutuante

divv = a // b
print(divv)
#Esse vai descartar o ponto flutuante e vai retornar apenas a parte inteira

mod = a % b
print(mod)
#Retorna o resto da divisão entre os operadores

expo = a ** b
print(expo)
#Vai elevar o primeiro operador a quantidade de vezes do segundo

#Comparação 

"""
igual ==
diferente !=
maior que >
menor que <
maior OU igual >=
menor OU igual <=
"""

#LÓGICOS

"""
Os operadores lógicos só trabalham com True ou False
"""

result = ( a < b) and ( b > 2)
print(result)
#Os dois têm q ser verdadeiros

result = ( a < b) or ( b > 5)
print(result)
#Pelo menos um tem q ser verdadeiro

result = not ( a < b)
print(result)
#Inverte o valor

"""
Python segue as regras de precedência: parênteses, exponenciação, multiplicação/divisão, soma/subtração, operadores de comparação e operadores lógicos.
"""