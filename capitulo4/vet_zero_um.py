"""
Algoritmo para preencher um vetor com 1 para posições pares e 0 para posições ímpares
"""

vet = [0] * 6

for i in range(len(vet)):
    if i%2 == 0:
        vet[i] = 1
    else:
        vet[i] = 0

print(vet)
