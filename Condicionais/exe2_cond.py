print("Digite as três medidas do lado de um triângulo:")

lado1 = float(input("Medida 1: "))
lado2 = float(input("Medida 2: "))
lado3 = float(input("Medida 3: "))

if lado1 == lado2 == lado3:
    print("Esse triângulo é equilátero")
elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado1 != lado2 == lado3:
    print("Esse triângulo é isósceles")
else:
    print("Esse triângulo é escaleno")