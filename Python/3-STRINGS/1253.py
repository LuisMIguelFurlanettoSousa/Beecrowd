n = int(input())
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for _ in range(n):
    palavra = list(input().upper())
    deslocamento = int(input())

    nova_palavra = []
    for l in palavra:
        if l in alfabeto:
            posicao_letra = alfabeto.index(l)
            index_letra = (posicao_letra - deslocamento) % len(alfabeto)
            nova_palavra.append(alfabeto[index_letra])

nova_palavra = "".join(nova_palavra)
print(nova_palavra)
