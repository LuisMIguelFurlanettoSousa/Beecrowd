valor = float(input())

# Converter o valor para centavos para evitar problemas de precisão
valor = int(round(valor * 100))

notas = [10000, 5000, 2000, 1000, 500, 200]  # Valores em centavos
moedas = [100, 50, 25, 10, 5, 1]
quantidadeNotas = []
quantidadeMoedas = []

# Calcular quantidade de notas
for n in notas:
    quantidade = valor // n
    quantidadeNotas.append(quantidade)
    valor %= n  # Atualizar o valor restante

# Calcular quantidade de moedas
for m in moedas:
    quantidade = valor // m
    quantidadeMoedas.append(quantidade)
    valor %= m  # Atualizar o valor restante

# Exibir o resultado
print("NOTAS:")
for i in range(len(notas)):
    print(f"{quantidadeNotas[i]} nota(s) de R$ {notas[i] // 100}.00")

print("MOEDAS:")
for i in range(len(moedas)):
    print(f"{quantidadeMoedas[i]} moeda(s) de R$ {moedas[i] / 100:.2f}")
