def substitui(t):
    conta_sublinhado = 0
    conta_asteristico = 0
    i = 0  # Índice manual para rastrear a posição no texto
    while i < len(t):
        if t[i] == "_" and conta_sublinhado == 0:
            conta_sublinhado = 1
            t = t[:i] + "<i>" + t[i + 1:]  # Substituir o "_"
            i += 3  # Avançar para ignorar o "<i>"
        elif t[i] == "_" and conta_sublinhado == 1:
            conta_sublinhado = 0
            t = t[:i] + "</i>" + t[i + 1:]  # Substituir o "_"
            i += 4  # Avançar para ignorar o "</i>"
        elif t[i] == "*" and conta_asteristico == 0:
            conta_asteristico = 1
            t = t[:i] + "<b>" + t[i + 1:]  # Substituir o "*"
            i += 3  # Avançar para ignorar o "<b>"
        elif t[i] == "*" and conta_asteristico == 1:
            conta_asteristico = 0
            t = t[:i] + "</b>" + t[i + 1:]  # Substituir o "*"
            i += 4  # Avançar para ignorar o "</b>"
        else:
            i += 1  # Avançar normalmente

    return t


# Entrada e saída
texto = input()
texto_html = substitui(texto)
print(texto_html)
