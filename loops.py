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

#CONTROLE DE LOOPS

"""
break
Quando um break é encontrado, o loop é interrompido e o fluxo de execução continua com a próxima instrução fora do loop
"""

i = 0
print("Início do while")
while i < 12:
    print(i)
    i += 1

    if i == 8:
        #IF verifica se esta contição foi atendida e quando for será executado o BREAK e WHILE será quebrado por completo e sairá do loop
        break
        
print("Fim do while")

for x in range(10):

    if x % 2 == 0:
        continue
    """
    Neste exemplo, o loop for itera sobre os números de 0 a 9 utilizando a função range(). Dentro do loop, verifica-se se o número é divisível por 2 utilizando o operador de módulo %. Se o número for divisível por 2 (ou seja, se for par), a instrução continue é executada, fazendo com que o restante do bloco de código seja pulado e passando para a próxima iteração do loop. Como resultado, apenas os números ímpares serão impressos.
    """
    print(x)
