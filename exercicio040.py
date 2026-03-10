soma = 0       # vai somar todas as temperaturas válidas
contador = 0   # vai contar quantas temperaturas foram digitadas

while True:
    temperatura = float(input("Digite a temperatura em Celsius (-273 para sair): "))
    
    if temperatura == -273:  # condição de parada
        break
    
    soma += temperatura      # adiciona a temperatura à soma
    contador += 1            # incrementa o contador

# verificar se houve pelo menos uma temperatura válida
if contador > 0:
    media = soma / contador
    print("Média das temperaturas:", media)
else:
    print("Nenhuma temperatura válida foi digitada.")