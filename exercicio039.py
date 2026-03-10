contador = 0
while contador <= 15:
    print("Digite a nota: ")
    nota = int(input())
    if nota < 0 or nota > 5:
        print("Nota inválida, digite novamente.")
    else:
        contador += 1