# exemplos de listas
# armazenar um conjunto de dados

# lista com 6 numeros inteiros
lista_numeros = [5, 7, 10, 12, 8, 4]

# unica forma de acessar, é pelo indice, de 0 a n (tamanho da lista)

# imprimir o terceiro elemento da lista_numero
print(f"Terceiro elemento da lista: {lista_numeros[2]}")

# imprimir o ultimo elemento da lista sem saber o ultimo elemento
print(f"Ultimo número da lista: {lista_numeros[-1]}")

#**Funções mais utilizadas em listas**
#Tamanho da lista: função len
tamanho_lista = len(lista_numeros)
print(f"Tamanho da lista: {tamanho_lista}")

# Somar os elementos da lista: função sum
print(f"Soma dos elementos: {sum(lista_numeros)}")

# Menor elemento da lista: função min
print(f"Menor elemento da lista: {min(lista_numeros)}")

# maior elemento da lista: função max
print(f"Maior elemento da lista: {max(lista_numeros)}")

# Solicitar ao usuário a digitação dos elementos de uma lista que deverá ter 10 palavras

#1ºcria uma lista vazia
lista_palavras = []
# 2º for para andar pela lista
for i in range(10): # i varia de 0 a 9
    palavra = input("Digite a palavra: ")
    lista_palavras.append(palavra) # insere elemento no final da lista

print(lista_palavras)

for palavra in lista_palavras:
    print(palavra)