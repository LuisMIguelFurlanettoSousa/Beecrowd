segundos = int(input())

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundosRestantes = segundos % 60

print(f"{horas}:{minutos}:{segundosRestantes}")