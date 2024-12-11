def combina(f1, f2):
    combinada = ""
    for i in range(min(len(f1), len(f2))):
        combinada += f1[i] + f2[i]

    if len(f2) > len(f1):
        combinada += f2[len(f1):]
    elif len(f2) < len(f1):
        combinada += f1[len(f2):]

    return combinada


reps = int(input())

for _ in range(reps):
    f1, f2 = input().split()

    strings_combinadas = combina(f1, f2)

    print(strings_combinadas)