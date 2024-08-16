'''
Faça um programa em Python que leia 10 números inteiros e armazene-os em uma lista. Em seguida, armazene os números pares na lista PAR e os números ÍMPARES na lista ímpar. Por fim, imprima as 3 listas.
'''

lista = []
lista_par = []
lista_impar = []

for i in range(10):
    num = int(input("Digite um número inteiro: "))
    lista.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)


print(f"Lista completa: {lista}")
print(f"Lista Par: {lista_par}")
print(f"Lista Impar: {lista_impar}")
