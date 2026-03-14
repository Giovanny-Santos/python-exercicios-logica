data = {}
invalido = 0
data["dia"] = int(input("Digite o dia: "))
if data["dia"] >= 1 and data["dia"] <= 31:
    print("Mês válido")
else:
    invalido += 1
data["mes"] = int(input("Digite o mês: "))
if data["mes"] >= 1 and data["mes"] <= 12:
    print("Mês válido")
else:
    invalido += 1
data["ano"] = int(input("Digite o ano: "))
if data["ano"] >= 0 and data["ano"] <= 2026:
    print("Mês válido")
else:
    invalido += 1

if invalido == 3:
    print("A data que voce colocou não existe")
else:
    print("A data que voce colocou existe")