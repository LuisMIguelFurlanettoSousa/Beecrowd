from math import gcd

def simplificar(n, d):
    divisor_comum = gcd(n, d)
    return n // divisor_comum, d // divisor_comum


def main():
    n = int(input())

    for _ in range(n):
        n1, _, d1, operacao, n2, _, d2 = input().split()
        n1, d1, n2, d2 = int(n1), int(d1), int(n2), int(d2)

        if operacao == '+':
            numerador = (n1 * d2) + (n2 * d1)
            denominador = d1 * d2
        elif operacao == '-':
            numerador = (n1 * d2) - (n2 * d1)
            denominador = d1 * d2
        elif operacao == '*':
            numerador = n1 * n2
            denominador = d1 * d2
        elif operacao == '/':
            numerador = n1 * d2
            denominador = n2 * d1

        if denominador < 0:
            numerador = -numerador
            denominador = -denominador

        resultado_nao_simplificado = f"{numerador}/{denominador}"

        num_simplificado, den_simplificado = simplificar(numerador, denominador)
        resultado_simplificado = f"{num_simplificado}/{den_simplificado}"

        print(f"{resultado_nao_simplificado} = {resultado_simplificado}")
        
if __name__ == "__main__":
    main()