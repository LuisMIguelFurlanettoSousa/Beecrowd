a, b, c = map(float, input().split())

tri = (a * c) / 2
pi = 3.14159
circ = pi * (c ** 2)
trap = ((a + b) * c) / 2
quad = b ** 2
ret = a * b

print(f"TRIANGULO: {tri:.3f}")
print(f"CIRCULO: {circ:.3f}")
print(f"TRAPEZIO: {trap:.3f}")
print(f"QUADRADO: {quad:.3f}")
print(f"RETANGULO: {ret:.3f}")