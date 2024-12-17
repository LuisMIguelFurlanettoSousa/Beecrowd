n = int(input())

for _ in range(n):
    dieta = list(input())
    manha = list(input())
    almoco = list(input())

    if not manha and not almoco:
        dieta_ordenada = sorted(dieta)
        nada = "".join(dieta_ordenada)
        print(nada)
        continue

    dia = sorted(manha[:] + almoco[:])
    Ncomida = []
    passou = True

    for v in dia:
        if v not in dieta:
            print("CHEATER")
            break
            passou = False

    if passou:
        for v in dieta:
            if v not in dia:
                Ncomida.append(v)
        Ncomida = sorted(Ncomida)
        Ncomida = "".join(Ncomida)
        print(Ncomida)
