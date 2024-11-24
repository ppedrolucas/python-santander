"""
O loop for é utilizado para iterar sobre uma sequência (como uma lista, uma tupla ou uma string) ou qualquer objeto iterável. A sintaxe básica é a seguinte:

for variável in sequência:

    # Bloco de código a repetir
    instruções

Ideal quando sabemos com antecedencia o número de iterações
"""

frutas = ["ryzen 5 5600Gt", "B550M Aorus Elite", "Corsair 550W", "1TB de ssd", "16GB de ram", "Gabinete pichau apus white"]

for fruta in frutas:
    print(fruta)

#WHILE Enquanto a condição for verdadeira, execute

contador = 0

while contador <= 10:
    print(contador)
    contador += 1

"""
Enquanto o contador for menor ou igual a 10, imprima na tela e dps incremente mais um

É importante ter cuidado ao usar o loop while, pois, se a condição nunca se tornar falsa, o loop será executado indefinidamente, o que é conhecido como um loop infinito.
"""