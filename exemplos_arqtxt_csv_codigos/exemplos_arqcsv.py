# Manipulação de arquivos csv
import csv

# Leitura do arquivo csv (forma 1)
with open("base_alunos.csv","r",encoding="utf-8") as arqAlunos:
    tabela = csv.reader(arqAlunos,delimiter=";")
    next(tabela)
    for linha in tabela:
        print(linha)
    arqAlunos.close()

# Leitura do arquivo csv (forma 2)
with open("base_alunos.csv","r",encoding="utf-8") as arqAlunos:
    tabela = csv.reader(arqAlunos,delimiter=";")
    next(tabela)
    for linha in tabela:
        print(f"Curso: {linha[0]}   Aluno: {linha[1]}")
    arqAlunos.close()

# Leitura do arquivo csv (forma 3)
with open("base_alunos.csv","r",encoding="utf-8-sig") as arqAlunos:
    dicionario = csv.DictReader(arqAlunos,delimiter=";")
    listaDicionario = list(dicionario)
    #print(listaDicionario)
    print(listaDicionario[2])
    print(listaDicionario[2]['Curso'])
