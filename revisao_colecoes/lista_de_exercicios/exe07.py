'''
Escreva um programa em Python que crie uma lista de 10 funcionários, 
utilizando o conceito de dicionários, contendo os seguintes dados:

o	Nome;
o	Cargo;
o	Salário.
Depois da lista criada, faça a busca pelo nome de um funcionário 
qualquer e mostre seus dados.
'''
lista_funcionario = []

for i in range(2):
    nome=input("Nome: ")
    cargo=input("Cargo: ")
    salario=float(input("Salário: "))
    print("------------------")

    funcionarios = {'Nome': nome, 'Cargo':cargo, 'Salario':salario}

    lista_funcionario.append(funcionarios)

def buscar_funcionario(nome, lista_funcionario):
    for funcionario in lista_funcionario:
        if funcionario["Nome"].lower() == nome.lower():
            return funcionario
    return "Funcionário não encontrado."

nome_funcionario = input("Digite o nome do funcionário que deseja buscar: ")

resultado = buscar_funcionario(nome_funcionario, lista_funcionario)
print(resultado)
