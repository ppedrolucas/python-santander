"""
Python nos permite ler e escrever dados em arquivos externos. Podemos abrir em diferentes modos, leitura "r", escrita "w" ou anexar "a".
"""
arquivo = open("dados.txt", "r") #Abrir o arquivo no modo leitura
conteudo = arquivo.read() #O conteúdo no arquivo é lido e armazenado na variável conteudo
print("1, ", conteudo) #Conteúdo é mostrado na tela
arquivo.close() #Arquivo é fechado

arquivo = open("dados.txt", "w") #Abrir arquivo no modo escrita para escrever dados
arquivo.write("Não posso parar") #Escrever conteúdo no arquivo
arquivo.close() #Fechamento do arquivo
print("2, ", conteudo) #Conteúdo mostrado na tela
