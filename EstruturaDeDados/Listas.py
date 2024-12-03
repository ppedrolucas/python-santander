"""
As estruturas de dados nos permitem organizar e armazenar dados de maneira eficiente em nossos programas. Python fornece várias estruturas de dados integradas, como listas, tuplas, dicionários e conjuntos, cada uma com suas próprias características e usos.
"""

#Listas/Arrays em Python - Criação e Acesso

listaDeCoisas = [2005, "pedro", "Ryzen 5 5600GT", 70.1, True]
#Posso criar uma lista com diferentes tipos de dados, para dizer que é uma lista basta agrupá-los entre colchetes.

#Acessar os elementos da lista 0 até N - 0, onde 0 é o primeiro elemento da lista e N - 0 é o último elemento dela.
#Posso também acessar os elementos a partir do final da lista utilizando indices negativos, onde o último é -1, penúltimo é -2 e assim por diante.
print(listaDeCoisas[3])

#Métodos de listas em python, esses métodos permitem manipular e modificar os elementos da lista.

#Exemplo:

frutas = ["Maçã", "Banana", "Uva"]
#print(frutas)

#Adicionar elemento ao final da lista
frutas.append("Pêra")
print(frutas)

#Insere um elemento a uma posição específica da lista
frutas.insert(0, "Morango")
print(frutas)

#Remove a primeira ocorrência de um elemento na lista
frutas.remove("Banana")
print(frutas)

#Com o pop eu removo um elemento da lista de acordo com seu indice e o retorno, com esse retorno eu posso armazenar o elemento removido em uma outra variável.
frutas_removida = frutas.pop(1)
print(frutas) #Fluxo normal da lista
print(frutas_removida) #Elemento removido

#Ordena os elementos da lista em ordem ascedente
frutas.sort()
print(frutas)

#Inverter a ordem dos elementos na lista
frutas.reverse()
print(frutas)