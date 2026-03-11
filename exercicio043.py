lista = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
acima_media = 0
porcentagem_total = len(lista)
for valor in lista:
    if valor > 3000:
        acima_media += 1
porcentagem = (acima_media / porcentagem_total) * 100
print(f"Existem {acima_media} valores acima de 3000, que representa {porcentagem:.2f}% do total.")