peca1, quant1, VUnid1 = input().split()

peca1 = int(peca1)
quant1 = int(quant1)
VUnid1 = float(VUnid1)

peca2, quant2, VUnid2 = input().split()

peca2 = int(peca2)
quant2 = int(quant2)
VUnid2 = float(VUnid2)

tot = (quant1 * VUnid1) + (quant2 * VUnid2)

print(f"VALOR A PAGAR: R$ {tot:.2f}")
