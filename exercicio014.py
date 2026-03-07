print("Digite o primeiro valor: ")
primeiro = input("")
print("Digite o segundo valor: ")
segundo = input("")
print("Digite o operador: ")
operador = input(" ")
print("digite a potencia: ")
potencia = input(" ")
if operador == "+":
    resultado = int(primeiro) + int(segundo)
    print("o valor da soma é: ", resultado)
if operador == "-":
    resultado = int(primeiro) - int(segundo)
    print("o valor da subtração é: ", resultado)
if operador == "*":
    resultado = int(primeiro) * int(segundo)
    print("o valor da multiplicação é: ", resultado)
if operador == "/":
    resultado = int(primeiro) / int(segundo)
    print("o valor da divisão é: ", resultado)
resultado = int(resultado) ** int(potencia)
print("o valor da potencia é: ", resultado)