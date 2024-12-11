def dancing(t):
    text_dance = []  # Lista para armazenar o texto formatado
    index = 0  # Índice alternado para controlar maiúsculas e minúsculas

    for char in t:  # Percorre cada caractere da string
        if char == " ":
            text_dance.append(char)  # Mantém os espaços
        else:
            if index % 2 == 0:
                text_dance.append(char.upper())  # Adiciona em maiúscula
            else:
                text_dance.append(char.lower())  # Adiciona em minúscula
            index += 1  # Incrementa o índice apenas para letras

    return "".join(text_dance)  # Junta a lista em uma string

text = input().upper()

dance = dancing(text)
print(dance)
