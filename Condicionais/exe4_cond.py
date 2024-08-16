# ano bissexto
ano = int(input("Digite um ano: "))

if 1999 <= ano <= 2999:
    print("Seu ano está dentro da faixa de 1000 a 2999")
    if ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0):
        print("Ano Bissexto")
    else:
        print("Seu ano NÃO é Bissexto")
else:
    print("Erro, reinicie o programa novamente")



