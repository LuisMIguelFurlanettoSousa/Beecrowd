valor = int(input())

# Inicializar as variáveis
notas100 = notas50 = notas20 = notas10 = notas5 = notas2 = notas1 = 0

# Exibir o valor inicial
print(valor)

# Calculando o número de notas para cada valor
if valor >= 100:
    notas100 = valor // 100
    valor -= notas100 * 100
if valor >= 50:
    notas50 = valor // 50
    valor -= notas50 * 50
if valor >= 20:
    notas20 = valor // 20
    valor -= notas20 * 20
if valor >= 10:
    notas10 = valor // 10
    valor -= notas10 * 10
if valor >= 5:
    notas5 = valor // 5
    valor -= notas5 * 5
if valor >= 2:
    notas2 = valor // 2
    valor -= notas2 * 2
if valor >= 1:
    notas1 = valor // 1
    valor -= notas1 * 1

# Exibir as quantidades de cada nota
print(f"{notas100} nota(s) de R$ 100,00")
print(f"{notas50} nota(s) de R$ 50,00")
print(f"{notas20} nota(s) de R$ 20,00")
print(f"{notas10} nota(s) de R$ 10,00")
print(f"{notas5} nota(s) de R$ 5,00")
print(f"{notas2} nota(s) de R$ 2,00")
print(f"{notas1} nota(s) de R$ 1,00")