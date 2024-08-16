'''
Desenvolva um programa que preencha um vetor com as idades dos usuários até que o usuário digite um valor negativo, o valor negativo não deve ser inserido na lista. Ao final, exiba na tela:
- A quantidade de usuários menores de 18 anos; 
- A média das idades
'''
idades = []

while True:
    idade = int(input("Digite a sua idade: "))
    if idade < 0: 
        break

    idades.append(idade)

menores_18 = len([idade for idade in idades if idade < 18])
media_idades = sum(idades)/len(idades)

print(f"Quantidade de usuários menores de 18 anos: {menores_18}")
print(f"Média das idades: {media_idades:.2f}")