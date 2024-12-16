import sys
import re

def calcular_dificuldade(enunciado):
    # Filtrar palavras válidas (apenas letras e podem terminar com um ponto único)
    palavras = re.findall(r'\b[a-zA-Z]+\.?\b', enunciado)
    
    # Calcular comprimento total das palavras válidas (ignorando o ponto final)
    comprimento_total = sum(len(palavra.rstrip('.')) for palavra in palavras)
    
    # Número de palavras
    num_palavras = len(palavras)
    
    # Calcular comprimento médio
    comprimento_medio = (comprimento_total // num_palavras) if num_palavras > 0 else 0
    
    # Determinar dificuldade com base no comprimento médio
    if comprimento_medio <= 3:
        return 250
    elif 4 <= comprimento_medio <= 5:
        return 500
    else:
        return 1000

# Ler entradas até EOF
for linha in sys.stdin:
    linha = linha.strip()
    if linha:
        dificuldade = calcular_dificuldade(linha)
        print(dificuldade)
