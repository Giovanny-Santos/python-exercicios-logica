print("escreva o primeiro valor: ")
valor1 = input()
print("escreva o segundo valor: ")
valor2 = input()
print("escreva o terceiro valor: ")
valor3 = input()

valor1 = int(valor1)
valor2 = int(valor2)
valor3 = int(valor3)

if valor1 > valor2 and valor1 > valor3:
    print("O maior valor é o primeiro: ", valor1)
    if valor2 < valor3:
        print("O menor valor é o segundo: ", valor2)
    else:
        print("O menor valor é o terceiro: ", valor3)



if valor2 > valor1 and valor2 > valor3:
    print("O maior valor é o segundo: ", valor2)
    if valor2 < valor3:
        print("O menor valor é o segundo: ", valor2)
    else:
        print("O menor valor é o terceiro: ", valor3)

if valor3 > valor1 and valor3 > valor2: 
    print("O maior valor é o terceiro: ", valor3)
    if valor2 < valor3:
        print("O menor valor é o segundo: ", valor2)
    else:
        print("O menor valor é o terceiro: ", valor3)