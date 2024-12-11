# nao consegui
import sys

def larger_substring(f1, f2):   
    larguer = 0

    # Gerar todas as substrings possíveis de f1
    for i in range(len(f1)):
        for j in range(i + 1, len(f1) + 1):
            substring = f1[i:j]

            # Contar ocorrências da substring em f2
            qnt_sub = f2.count(substring)
            if qnt_sub > larguer:
                larguer = qnt_sub

    return larguer




for line in sys.stdin:
    phrase_1 = input()
    phrase_2 = input()

    larger = larger_substring(phrase_1, phrase_2)
    print(larger)
