print("Digite um número inteiro: ")
num = int(input())
print("Digite segundo número inteiro: ")
num2 = int(input())

if num > num2:
    contador = num - num2
    while contador <= num:
        print(contador)
        contador += 1
else:
    contador = num2 - num
    while contador <= num2:
        print(contador)
        contador += 1
