rep = int(input())

for _ in range(rep):
    tokens = input().split()

    numeros = [int(x) if x.isdigit() else x for x in tokens]
    
    n2 = numeros[0]
    d1 = numeros[2]
    n2 = numeros[4]
    d2 = numeros[6]
    operador = numeros[3]


    Sub = (n2*d2 - n2*d1) / (d1*d2)
    Multi = (n2*n2) / (d1*d2)
    Div = (n2*d2)/(n2*d1)

    if operador == '+':
        Soma =  (n2*d2 + n2*d1) / (d1*d2)
        print(Soma)




    #1 / 2 + 3 / 4