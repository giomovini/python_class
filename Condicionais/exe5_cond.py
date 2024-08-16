"""
- solicitar os 4 números
- armazenar em variaveis
- ordená-los em ordem crescente
"""

print("Digite 4 números: ")
nm1 = int(input("1º número: "))
nm2 = int(input("2º número: "))
nm3 = int(input("3º número: "))
nm4 = int(input("4º número: "))

lista = [nm1, nm2, nm3, nm4]
lista.sort()
print(lista)

print("---------------------------")

lista2 = []
qnt = 4

for i in range(qnt):
    elemento = int(input("Digite um número: "))
    lista2.append(elemento)

lista2.sort()
print(lista2)


"""
método "sort()", é uma função do Python que ordena uma lista em ordem crescente de forma automática, modificando a lista e reordenando os elementos 

método "sorted()", é igual ao metodo sort(), porém ela armazena a lista original e cria uma nova lista ordenada de forma crescente
"""