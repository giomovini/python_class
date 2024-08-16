def soma_digitos(numero):
    # Inicializa a soma dos dígitos
    soma = 0
    
    # Converte o número para uma string para iterar sobre os dígitos
    numero_str = str(numero)
    
    # Itera sobre cada dígito na string
    for digito in numero_str:
        # Converte o dígito de volta para inteiro e adiciona à soma
        soma += int(digito)
    
    return soma

# Solicita o número ao usuário
numero = int(input("Digite um número: "))

# Chama a função para somar os dígitos do número
resultado = soma_digitos(numero)

# Exibe o resultado
print(f"A soma dos dígitos de {numero} é {resultado}.")
