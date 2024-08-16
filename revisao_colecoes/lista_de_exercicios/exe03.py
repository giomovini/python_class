'''
Faça um programa em Python que peça as 3 notas de 10 alunos, calcule e armazene em uma lista a média de cada aluno. Em seguida, imprima o número de alunos com média maior ou igual a 7.0.

Crie uma lista para as médias e um contador de alunos.
Para cada um dos 10 alunos:
    Peça as 3 notas.
    Calcule a média.
    Armazene a média na lista.
Se a média for maior ou igual a 7.0, incremente o contador.
Após o laço, exiba o número de alunos com média maior ou igual a 7.0.
'''
contador_aluno = 0
media = []
for i in range(10):
    nota01 = float(input("Nota 01: "))
    nota02 = float(input("Nota 02: "))
    nota03 = float(input("Nota 03: "))
    print("-----------------")
    media_notas = (nota01+nota02+nota03)/3
    media.append(media_notas)
    if media_notas >= 7.0:
        contador_aluno = contador_aluno + 1
print(f"Número de alunos com média maior ou igual a 7: {contador_aluno}")
    




