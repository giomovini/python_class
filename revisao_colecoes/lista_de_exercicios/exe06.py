'''
Escreva um programa que simule um dicionário inglês/português utilizando o conceito de listas. 
Para tanto, crie uma lista para as palavras em inglês e outra para as traduções em 
português nas respectivas posições. 
A inserção das palavras deverá ser executada até que o usuário 
digite uma opção de saída 0 (Deseja continuar (1-SIM / 0-NÃO). 
Após a inserção, exiba a tradução em português de uma determinada palavra em inglês que o usuário deverá digitar.
'''

palavras_ingles = []
palavras_portugues = []

while True:
    continuar = input("Deseja continuar inserindo palavras? (1-SIM / 0-NÃO): ")
        
    if continuar == '0':
        break
    elif continuar == '1':
        palavra_ingles = input("Digite a palavra em inglês: ").strip()
        palavra_portugues = input("Digite a tradução em português: ").strip()
            
        palavras_ingles.append(palavra_ingles)
        palavras_portugues.append(palavra_portugues)
    else:
        print("Opção inválida! Por favor, digite 1 para SIM ou 0 para NÃO.")

while True:
    palavra_a_traduzir = input("Digite a palavra em inglês que deseja traduzir (ou 'sair' para encerrar): ").strip()
        
    if palavra_a_traduzir.lower() == "sair":
        break

    if palavra_a_traduzir in palavras_ingles:
        # Obtém a posição da palavra na lista de palavras em inglês
        posicao = palavras_ingles.index(palavra_a_traduzir)
        # Usa a posição para encontrar a tradução correspondente na lista de palavras em português
        traducao = palavras_portugues[posicao]
        print(f"A tradução de '{palavra_a_traduzir}' é '{traducao}'.")
    else:
        print(f"A palavra '{palavra_a_traduzir}' não foi encontrada no dicionário.")
