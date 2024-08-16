def contar_pares_impares(num1, num2):
    pares = 0
    impares = 0
    
    # Verifica qual é o menor e o maior número
    menor = min(num1, num2)
    maior = max(num1, num2)
    
    # Percorre todos os números entre o menor e o maior
    for num in range(menor, maior + 1):
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    return pares, impares

# Solicita os números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Chama a função para contar os pares e ímpares
num_pares, num_impares = contar_pares_impares(num1, num2)

# Exibe o resultado
print(f"Entre {num1} e {num2} há {num_pares} números pares e {num_impares} números ímpares.")
