"""
As estruturas de controle nos permitem controlar o fluxo de execução de nossos programas. Em Python, as estruturas de controle mais comuns são as estruturas condicionais e os loops. Essas estruturas nos permitem tomar decisões e repetir blocos de código segundo certas condições.
"""

#Estrura condicional IF e IF/ELSE
idade = 18

if idade >= 18:
    print("Maior de idade")
    #Se a condição for verdadeira o print será executado, caso contrário nada acontecerá

novaIdade = 15

if novaIdade >= 18:
    print("Maior de idade")
else:
    print("É uma criança ainda")

media = 6

if media >= 9:
    print("Muito bom")
elif media >= 8:
    print("Bom")
elif media >=7:
    print("Quase hein")
else:
    print("Você falhou com essa cidades")