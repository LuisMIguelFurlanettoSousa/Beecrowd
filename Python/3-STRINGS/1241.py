# • verificar se B corresponde aos ultimos digitos de A
# • entrada com casos de testes ex: 4 
def verificacao(a, b):
    tam_b = len(b)
    ultimas_a = a[-tam_b::1]

    if b in ultimas_a:
        saida = "encaixa"
    else:
        saida = "nao encaixa"

    return saida

n = int(input())

for _ in range(n):
    a, b = input().split()
    resp = verificacao(a, b)
    print(resp)