#Entrada de dados
"""
nome = input("Insera seu nome aqui")
idade = input("Insira sua idade")
"""
#"input()" É uma função que mostra um mensagem da tela e espera o usuário digitar um valor.

#print("Olá" + nome + "com " + idade)

"""
Vale lembrar que a função input() sempre retornará uma cadeia de caracteres e para trabalhar com outros tipos de dados eu preciso converter o valor da função, usando funções como int() ou float()
"""

idade = int(input("Insira sua idade aqui: "))
nome = input("Insira seu nome aqui: ")

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade")

#Em saída de dados podemos usar a f-string (formatação para cadeias) para inserir variáveis diretamente de uma cadeia de texto. É tipo o Templete Literals do JS.

print(f"Olá {nome}, é um prazer em conhece-lo, você tem {idade} anos")