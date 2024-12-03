"""
Funções

Blocos que código que executam alguma tarefa específica e posso reutilizar essa função em vários locais diferentes do programa.
"""

#Definição de funções em Python

def nomeDaFuncao():
#Usa-se a palavra reservada DEF e o nome da função seguida de ":"
    i = 0
    while i <= 5:
        print("Olá mundo", i)
        i += 1

#Chamando função
nomeDaFuncao()

#Parâmetros, são os valores passados à função quando ela é chamada, nesse caso é "nome"
def saudacao(nome):
    print(f"Olá, {nome}!")

#Argumento que será passado ao parâmetro da função
saudacao("Pedro")
saudacao("Ramon Dino")

#As funções podem retornar valores ao serem chamadas
def soma(a, b):
    return a + b

resultado = soma(32, 128)
print(resultado)

#Python permite criar funções sem um nome de definição, é uma "função anônima ou lambda", são definidas em uma única linha e comumente usadas para funções pequenas, exemplo:

exponenciacao = lambda x: x ** 2
print(exponenciacao(12))

"""
IMPORTANTE

As variáveis definidas dentro de uma função têm um escopo local, o que significa que só são acessíveis dentro da função. Por outro lado, as variáveis definidas fora de qualquer função têm um escopo global e podem ser acessadas de qualquer parte do programa.
"""

def calcularMedia(*numeros): #Este asterísco significa que posso enviar quantos argumentos eu quiser para a função, será várias cópias do mesmo parâmetro.
    soma = sum(numeros) #Função que soma os elementos da Tupla
    quantidade = len(numeros) #Função que retorna a quantidade de elementos da Tupla
    media = soma / quantidade
    return media

print("Média: ",calcularMedia(10, 20, 30, 50, 80))

#Docstrings são cadeias de texto que descrevem o propósito da função, os parâmetros e etc...
def areaRetangulo(base, altura):
    """
    Calcular a área de um retângulo.
    
    Args:
        base: A base do retânglo.
        altura: A altura do retângulo.
        
    Returns:
        float: A área do retângulo.
        
    """
    return base * altura