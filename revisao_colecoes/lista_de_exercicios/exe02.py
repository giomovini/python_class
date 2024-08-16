'''
Faça um programa em Python que leia duas listas com 10 elementos cada. 
Gere uma terceira lista de 20 elementos, cujos valores deverão ser compostos 
pelos elementos intercalados das 2 listas.
'''

lista_1 = []
lista_2 = []
lista_intercalada = []

for i in range(10):
    num = int(input("Digite um número inteiro: "))
    lista_1.append(num)
print(lista_1)

for i in range(10):
    num = int(input("Digite um número inteiro: "))
    lista_2.append(num)
print(lista_2)

for i in range(len(lista_1)):
    lista_intercalada.append(lista_1[i])
    lista_intercalada.append(lista_2[i])

print(lista_intercalada)