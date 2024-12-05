q = int(input())
resultados = []

for c in range(q):
    n, p = map(int, input().split())
    pessoas = list(range(1, n + 1))

    index = 0
    while len(pessoas) > 1:
        index = (index + p - 1) % len(pessoas)
        pessoas.pop(index)

    resultados.append(pessoas[0])

for i, v in enumerate(resultados):
    print(f"case {i + 1}: {v}")
