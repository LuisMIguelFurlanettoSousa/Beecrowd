valor = float(input())

valores = ("[0,25]", "(25,50]", "(50,75]", "(75,100]")

if valor >= 0 and valor <= 25:
    print(f"Intervalo {valores[0]}")
elif valor > 25 and valor <= 50:
    print(f"Intervalo {valores[1]}")
elif valor > 50 and valor <= 75:
    print(f"Intervalo {valores[2]}")
elif valor > 75 and valor <= 100:
    print(f"Intervalo {valores[3]}")
else:
    print("Fora de intervalo")
