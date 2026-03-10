print("Digite um número inteiro: ")
num = int(input())
faturação = num
while faturação > 0:
    print(str(num) + " x " + str(faturação) + " = " + str(num * faturação))
    faturação += -1