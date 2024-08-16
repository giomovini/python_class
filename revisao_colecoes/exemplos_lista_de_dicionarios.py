# Lista de dicionários

# Exemplo criar uma lista de dicionários para armazenar dados de 5 alunos

lista_alunos = []

for i in range(3):
    rm = int(input("RM: "))
    nome = input("Nome: ")
    curso = input("Curso: ")
    disciplina = input("Disciplina: ")
    nota = float(input("Nota: "))
    
    aluno = {'RM': rm, 'Nome':nome, 'Curso':curso, 'Disciplina':disciplina, 'Nota':nota}

    lista_alunos.append(aluno)

for i in range(len(lista_alunos)):
    print(f"ALUNO {i+1}:")
    for chave, valor in lista_alunos[i].items():
        print(f"{chave}: {valor}")
    print("----------------------------------")

#Exibir somente os alunos que cursam TSC
for i in range(len(lista_alunos)):
    if(lista_alunos[i]['Curso'] == 'TSC'):
        for chave, valor in lista_alunos[i].items():
            print(f"{chave}: {valor}")
        print("----------------------------------")