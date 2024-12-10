def verificaDigito(d, n):
    # Remove todas as ocorrências do dígito d
    numberlist = [x for x in n if x != d]
    
    # Se, após a remoção, a lista está vazia ou contém apenas zeros, retorne 0
    if not numberlist or all(x == '0' for x in numberlist):
        return 0
    
    # Retorne o número formado pelos dígitos restantes
    return int("".join(numberlist))

while True:
    d, n = input().split()  # Lê os valores d e n como strings
    if d == '0' and n == '0':  # Condição de parada
        break
    digit = verificaDigito(d, n)
    print(digit)