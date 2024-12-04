x = int(input())

ano = x // 365
mes = (x % 365) // 30
dia = ((x % 365) % 30)

print(f"{ano} ano(s)\n"
    f"{mes} mes(es)\n"
    f"{dia} dia(s)")