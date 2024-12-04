a, b, c = map(float, input().split())

delta = x1 = x2 = 0
if a == 0:
    print("Impossivel calcular")
else:
    delta = b * b - 4 * a * c

    if delta < 0:
        print("Impossivel calcular")
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
    
        print(f"R1 = {x1:.5f}\n"
            f"R2 = {x2:.5f}")
