peso = int(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

imc = peso / altura ** 2
print("Seu IMC = ", imc)
if(imc < 18.5):
    print("Abaixo do peso")
elif(18.5 < imc < 24.9):
    print("Peso Ideal, PARABÉNS")
elif(25.0 < imc < 29.9):
    print("Levemente acima do peso")
elif(30.0 < imc < 34.9):
    print("Obesidade grau 1")
elif(35.0 < imc < 39.9):
    print("Obesidade grau 2 (severa)")
elif(imc >= 40.0):
    print("Obesidade grau 3 (mórbida)")
