print ("Digite um numero inteiro: ")
num = int(input())
numero_primo = []
for i in range(2, num + 1):
    divisores = 0
    for j in range(2, num + 1):
        if i % j == 0:
            divisores += 1

    if divisores == 1:
        numero_primo.append(i)

print("Os números primos entre 1 e " + str(num) + " são: ", numero_primo)

    

