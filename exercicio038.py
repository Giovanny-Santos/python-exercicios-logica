
coloniaA = 4
coloniaB = 10

crescimentoA = 0.03
crescimentoB = 0.015
dias = 0
while coloniaA < coloniaB + 1:
    coloniaA += coloniaA * crescimentoA
    coloniaB += coloniaB * crescimentoB
    dias += 1

print("Dias necessários para a colônia A ultrapassar a colônia B: ", dias)
print("Colônia A: ", int(coloniaA))
print("Colônia B: ", int(coloniaB))

