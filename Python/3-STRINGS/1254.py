# nao consegui
while True:
    try:
        palavra = input()
        substituir = input()
        frase = input()

        primeiro = segundo = False
        frase_covertida = ""
        nova_frase = []
        
        for c in range(len(frase)):
            if frase[c] == "<":
                primeiro = True
                nova_frase.append(frase[c])
            elif primeiro and frase[c] == ">":
                segundo == True

            if primeiro and segundo:
                frase_covertida = frase.replace(palavra, substituir)

        print(frase_covertida)

    except EOFError:
        break
