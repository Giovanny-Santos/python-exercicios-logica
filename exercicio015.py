print("Digite o primeiro valor: ")
primeiro = input(" ")
print("Digite o denominador: ")
denominador = input(" ")
if denominador == "0":
    print("Não é possivel dividir por zero")
else:
    resultado = int(primeiro) // int(denominador)
    print("o valor da divisão é: ", resultado)
    