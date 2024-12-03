"""
Conjuntos (set)
 
Um conjunto é uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos únicos. Os conjuntos são delimitados por chaves {} ou são criados utilizando a função set().
"""

#Criação e operações com conjuntos
frutas = {"maçã", "banana", "tomate"}
#as duas formas estão corretas
numeros = set([1, 2, 3, 4, 5])

conjuntoA = {1, 2, 3}
conjuntoB = {3, 4, 5}

#Operações dos conjuntos igual na matemática
uniao = conjuntoA | conjuntoB
print("União dos conjuntos", uniao)

intersecao = conjuntoA & conjuntoB
print("Interseção dos conjuntos", intersecao)

diferenca = conjuntoA - conjuntoB
print("Diferênça dos conjuntos A - B", diferenca)

#Métodos de conjuntos em python

#adiciona um elemento
frutas.add("pera")
print(frutas)

#remove um elemento do conjunto. Se o elemento não existir, gera um erro.
frutas.remove("tomate")
print(frutas)

#remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
frutas.discard("uva")
print(frutas)

#remove todos os elementos do conjunto
frutas.clear()
print(frutas)