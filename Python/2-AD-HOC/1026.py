import sys

def main():
    try:
        for line in sys.stdin:
            # Lê os dois números da linha de entrada
            a, b = map(int, line.split())
            # Realiza a soma estilo "Mofiz" usando XOR
            result = a ^ b
            # Imprime o resultado
            print(result)
    except EOFError:
        pass

if __name__ == "__main__":
    main()
