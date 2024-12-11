def contLed(n):
    leds = {"1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6, "0": 6}
    soma = 0

    for i in n:
        soma += leds[i]
    return soma


qnt = int(input())

for _ in range(qnt):
    num = input()
    qnt_led = contLed(num)
    print(f"{qnt_led} leds")