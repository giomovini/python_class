'''
Desenvolva um programa que recebe 10 números inteiros e os armazene em uma lista. 
Em seguida, exiba quantos números múltiplos de 3 ela possui.
'''
lista = []

for i in range(10):
    numeros = int(input("Digite um número: "))
    lista.append(numeros)

multiplos_de_tres = 0
for numeros in lista:
        if numeros % 3 == 0:
            multiplos_de_tres += 1

print(f"Existem {multiplos_de_tres} números que são multiplos de 3")