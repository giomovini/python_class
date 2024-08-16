from collections import defaultdict

# Função map: conta as ocorrências de cada palavra
def map_function(words):
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    return word_count.items()

# Função Reduce: soma as contagens de ocorrências de palavras
def reduce_function(mapped_values):
    word_count = defaultdict(int)
    for word, count, in mapped_values:
        word_count[word] += count
    return word_count.items()

# Dados de entrada (lista de palavras)
input_data = ["olá", "Fiap", "olá", "Olá", "mundo", "python", "olá mundo", "mundo", "fiap", "Olá Fiap"]

# Fase Map: Aplica a função map para contar as palavras
mapped_values = map_function(input_data)

# Fase Reduce: Aplica a função reduce para agregar as contagens de palavrass
word_counts = reduce_function(mapped_values)

# Exibe o resultado
for word, count in word_counts:
    print(f"{word}: {count}")