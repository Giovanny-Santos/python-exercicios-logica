lista = []
for i in range(5):
    print("Digite um número: ")
    lista.append(float(input()))
    listareverse = lista[::-1]
print("Os números digitados foram: ", lista)
print("Os números digitados em ordem reversa foram: ", listareverse)