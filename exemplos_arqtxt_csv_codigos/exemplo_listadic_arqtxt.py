# Criar um arquivo texto com os dados de uma lista de contatos
lista_contatos = []

for i in range(5):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    idade = int(input("Idade: "))
    print("--------------------------")
    contato = {'Nome':nome,'Telefone':telefone,'Email':email,'Idade':idade}
    lista_contatos.append(contato)

for contato in lista_contatos:
    texto = f"{contato['Nome']}"+"\t"+f"{contato['Telefone']}"+"\t"+f"{contato['Email']}"+"\t"+f"{str(contato['Idade'])}"+"\n"
    with open("contatos.txt","a",encoding="utf-8") as arqContato:
        arqContato.write(texto)
        arqContato.close()