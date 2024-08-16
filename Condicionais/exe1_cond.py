media_anual = float(input("Digite sua média anual: "))

if media_anual >= 5.0:
    print("Aprovado!!")
elif 4.0 <= media_anual < 5.0:
    print("Exame")
else:
    print("Reprovado :(")