print("escreva a porcentagem de crescimento da produção: ")
produção = float(input())
if produção > 0:
    print("A produção está crescendo.")
elif produção < 0:
    print("A produção está diminuindo.")
else:
    print("A produção está estável.")
