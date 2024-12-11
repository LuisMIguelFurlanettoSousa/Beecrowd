import sys

for entrada in sys.stdin:
    try:
        # Lê os parâmetros de entrada
        max_palavras, max_linhas_pagina, max_caracteres_linha = map(int, entrada.strip().split())
        palavras = input().split()

        # Contadores
        linhas = 0
        paginas = 1
        caracteres_linha_atual = 0

        # Processa cada palavra
        for palavra in palavras:
            # Verifica se a palavra cabe na linha atual
            if (len(palavra) + caracteres_linha_atual) + (1 if caracteres_linha_atual > 0 else 0) <= max_caracteres_linha:
                caracteres_linha_atual += len(palavra) + (1 if caracteres_linha_atual > 0 else 0)
            else:
                # Inicia uma nova linha
                linhas += 1
                caracteres_linha_atual = len(palavra)

                # Se exceder o limite de linhas por página, conta uma nova página
                if linhas >= max_linhas_pagina:
                    paginas += 1
                    linhas = 0

        # Considera a última linha, caso ainda haja palavras nela
        if caracteres_linha_atual > 0:
            linhas += 1
            if linhas > max_linhas_pagina:
                paginas += 1

        # Exibe o número de páginas
        print(paginas)

    except EOFError:
        break