nome = input()
salarioF = float(input())
totVendas = float(input())

comicao = totVendas * (15 / 100)
salarioB = salarioF + comicao
print(f"TOTAL = R$ {salarioB:.2f}")
