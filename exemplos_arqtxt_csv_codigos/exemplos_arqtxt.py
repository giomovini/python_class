# Manipulação de arquivos texto no Python

# Abertura de um arquivo texto
# Traz uma linha do arquivo
with open("produtos_livraria.txt","r",encoding="utf-8") as arqLivraria:
    linha = arqLivraria.readline()
    print(linha)
    arqLivraria.close()

# Traz várias linha do arquivo (lista)
with open("produtos_livraria.txt","r",encoding="utf-8") as arqLivraria:
    linhas = arqLivraria.readlines()
    print(linhas)
    arqLivraria.close()

# Gravação no arquivo texto do zero
with open("produtos_farmacia.txt","w",encoding="utf-8") as arqFarmacia:
    texto = f"Sabonete  150  3.50"
    arqFarmacia.write(texto)
    arqFarmacia.close()

# Gravação no arquivo texto que já existe
with open("produtos_livraria.txt","a",encoding="utf-8") as arqLivraria:
    texto = f"\nCaderno  50  20.70"
    arqLivraria.write(texto)
    arqLivraria.close()
