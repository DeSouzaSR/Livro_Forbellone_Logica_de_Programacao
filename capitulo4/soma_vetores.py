"""
Programa  que lẽ, soma e imprime o resultado da soma entre dois vetores
"""

vet1 = [0] * 5
vet2 = [0] * 5
vetr = [0] * 5

for i in range(5):
    vet1[i] = int(input())
    vet2[i] = int(input())
    vetr[i] = vet1[i] + vet2[i]
    print(f'{vet1[i]} + {vet2[i]} = {vetr[i]}')