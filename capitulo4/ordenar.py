
N = 5

vetor = [0] * N

# Ler o vetor
for i in range(len(vetor)):
    vetor[i] = int(input)

# Perccorrer o vetor para encontrar o maior elemento
maior = vetor[0]
for i in range(1: len(vetor)):
    if vetor[i] > maior:
        maior = vetor[i]
        