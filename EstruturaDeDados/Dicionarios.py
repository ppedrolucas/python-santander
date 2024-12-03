"""
Dicionários

Um dicionário é uma estrutura de dados mutável e não ordenada que permite armazenar pares de chave-valor. Cada elemento em um dicionário consiste em uma chave única e seu valor correspondente. Os dicionários são delimitados por chaves {}, e os pares chave-valor são separados por vírgulas.

São tipo objetos no JS
"""

#Criar e acessar um dicionário
pessoa = {"nome":"Pedro", "idade":19, "cidade":"Pacajus"}

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])

#Métodos de dicionários

#Retorna as chaves do dicionário
print(pessoa.keys())

#Retorna os valores das chaves dentro do dicionário
print(pessoa.values())

#Retorna uma visualização de todos os pares-chaves do dicionário
print(pessoa.items())

#Atualiza o dicionário com um novo par de chave
pessoa.update({"profissao":"Assistente de Programação"})
print(pessoa)