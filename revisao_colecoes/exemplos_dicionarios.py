# Exemplos de dicionários

# variável que possui "itens", composto por uma chave/valor

# Dicionario para armazenar dados de um aluno
aluno = {'RM':1234, 'Nome':"Vinicius Cremon", 'Curso': "Data Science", 'Disciplina':"Python", 'Media':8.5}

# Exibir o curso do aluno
print(f"Curso do Aluno: {aluno['Curso']}")

# Exibir o dicionario completo
print(aluno)

# Função items: permite acessar o item (chave + valor)
for chave,valor in aluno.items():
    print(f"{chave}: {valor}")

# Função keys: permite acessar somente as chaves do dicionário
print(aluno.keys())

# Função values: permite acessar somente os valores do dicionário
print(aluno.values())