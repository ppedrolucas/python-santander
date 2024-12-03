"""
Tuplas

Tupla é uma estrutura de dados imutável, o que significa que não podem ser modificadas uma vez criadas. Não se pode adicionar, remover ou alterar elementos em uma tupla existente. Para criar uma tupla basta agrupar os elemetos entre parênteses.

As tuplas são úteis quando você precisa armazenar uma coleção de elementos que não devem ser modificados, como coordenadas ou dados de configuração.

Tupla é ordenada.
"""

minha_tupla = (1, 20, 17, 23, 22, 22, 6)

#Acessar os elementos de uma tupla:
print(minha_tupla[1])

#Retorna o número de vezes que um elemento aparece na tupla
print(minha_tupla.count(22))

#Retorna o índice da primeira aparição do elemento na tupla
print(minha_tupla.index(22))

#Retorna a quantidade de elementos da tupla
print(len(minha_tupla))