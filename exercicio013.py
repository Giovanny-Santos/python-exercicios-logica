print("Digite o valor: ")
primeiro = input("")
print("digite o valor do denominador: ")
segundo = input(" ")
if int(segundo) == 0:
    print("Não é possivel dividir por zero")
else:
    terceiro = int(primeiro) / int(segundo)
    print("o valor da divisão é: ", terceiro)
    