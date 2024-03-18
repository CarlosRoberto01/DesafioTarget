
#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:

#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

#b) Evite usar funções prontas, como, por exemplo, reverse;

def inverte_string(palavra):
    return palavra[::-1]

palavra = input(f"Escreva uma palavra e o programa ira invverter todos os caracteres: ")
palavra_invertida = inverte_string(palavra)
print(palavra_invertida)