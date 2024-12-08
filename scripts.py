#Manejo de execeções

#ELe nos permite capturar e lidar com erros de maneira mais controlada utilizando as declarações try, except e finally

#TRY

"""
try:
    resultado = 10 / 0
    print(resultado)
   
    Dentro do try contém um código que pode gerar uma exceção, se a exceção do try ocorrer, o fluxo de execução será transferido para o bloco except imediatamente

    Try funciona como um IF, se a condição do try for atendida, então o fluxo será transferido para o Except
    
except ZeroDivisionError:
    print("Err0: Divisão de zero")
"""


"""
Except é o bloco que especifica o tipo da exceção e que se deseja capturar, posso implementar vários except no mesmo try
"""

try:
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("Erro! Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")

#FINALLY é opcional e é executado sempre que uma exceção for ocorrida ou não. É comumente utilizado para tarefas de limpeza ou liberação de recursos.
try:
    # Código que pode gerar uma exceção
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção

