#Nao consegui fazer

def dancing(t):
    text_dance = []  # Lista para armazenar o texto formatado
    index = 0  # Índice alternado para controlar maiúsculas e minúsculas

    for char in t:  # Percorre cada caractere da string
        if char == " ":
            text_dance.append(char)
            continue

        if char == "a":
            if index % 2 == 0:
                text_dance.append(char.upper())
            else:
                text_dance.append(char.lower()) 
        elif char == t[-1]:
            text_dance.append(char.upper())
        elif index % 2 == 0:
            text_dance.append(char.upper())  # Adiciona em maiúscula
        elif index % 2 != 0:
            text_dance.append(char.lower())  # Adiciona em minúscula

        index += 1  # Incrementa o índice apenas para letras

    return "".join(text_dance)  # Junta a lista em uma string

text = input().lower()

dance = dancing(text)
print(dance)
