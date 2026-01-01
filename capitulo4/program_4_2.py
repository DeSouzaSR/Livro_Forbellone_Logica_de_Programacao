"""
Ler um vetor com 10 posições reais e calcular a média deste vetor. Num outro vetor armazenar a diferença absoluta entre o valor do vetor original e a média. 
"""

# Inicialização
vet_lido = [0.0] * 10
vet_des = [0.0] * 10

# Leitura do vetor
for i in range(10):
    vet_lido[i] = float(input('Enter vet values: '))

# Cálculo da média
media_lido = sum(vet_lido)/10

# Cálculo dos desvios
for i in range(10):
    vet_des[i] = abs(vet_lido[i] - media_lido)

# Cálculo da média dos desvios
media_des = sum(vet_des) /  10

print(f'\nMédia lido: {media_lido}\n')
print(f'Média des: {media_des}\n')