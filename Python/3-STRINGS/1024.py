def criptogrfia(frase):
    def primeira(f):
        frase_separada = list(f)
        frase_ascii_separada = []

        offset = 3

        for i in frase_separada:
            if i.islower() or i.isupper():
                frase_ascii_separada.append(chr(ord(i) + offset))
            else:
                frase_ascii_separada.append(i)

        return ''.join(frase_ascii_separada)

    def segunda(f):
        return f[::-1]

    def terceira(f):
        frase_separada = list(f)
        seguda_metade = len(frase_separada) // 2
        frase_ascii_separada = []
        metade = []

        offset = 1

        for i in frase_separada:
            frase_ascii_separada.append(chr(ord(i)))

        for l in range(len(frase_separada)):
            if l >= seguda_metade:
                metade.append(chr(ord(frase_separada[l]) - offset))

        
        return "".join(frase_separada[:seguda_metade] + metade)
    
    resultado = primeira(frase)
    resultado = segunda(resultado)
    resultado = terceira(resultado)
    
    return resultado

num = int(input())
listaFraseCripto = []

for _ in range(num):
    frase = input()
    fraseCriptografada = criptogrfia(frase)
    listaFraseCripto.append(fraseCriptografada)

for i in range(len(listaFraseCripto)):
    print(listaFraseCripto[i])

