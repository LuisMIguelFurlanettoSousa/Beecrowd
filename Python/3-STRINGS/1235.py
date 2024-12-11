def decifra(frase):
    tamanho = len(frase)
    metade = tamanho // 2

    metade_esquerda = frase[:metade]
    metade_direta = frase[metade:]

    return metade_esquerda[::-1] + metade_direta[::-1]

n = int(input())

for _ in range(n):
    frase = input().upper()
    frase_decifrada = decifra(frase)
    print(frase_decifrada)

# 5
# I ENIL SIHTHSIREBBIG S
# LEVELKAYAK
# H YPPAHSYADILO
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# VOD OWT SNEH HCNERF EGDIRTRAP A DNA SE