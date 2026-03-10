# refazer esse exercicio depois de aprender a usar listas, para armazenar as temperaturas e calcular a média depois
soma = 0
contador = 0 
while True:
    temperatura = float(input("Digite a temperatura em Celsius (-273 para sair): "))
    if temperatura == -273:
        break
    soma += temperatura
    contador += 1
if contador > 0:
    media = soma / contador
    print("Média das temperaturas:", media)
else:
    print("Nenhuma temperatura válida foi digitada.")